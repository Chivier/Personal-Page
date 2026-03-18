#!/usr/bin/env bash
set -euo pipefail

# Smart deploy script:
#   1. Compile CV (xelatex) so PDFs are up-to-date
#   2. Commit all source changes to main (codex-generated message)
#   3. Push main to remote
#   4. Build site (generator.py) and push dist/ to gh-pages
#
# Usage: ./deploy.sh [commit message]
#
# Prerequisites: Python deps installed, xelatex optional (for CV compilation).
# GitHub Pages should be configured to deploy from the gh-pages branch.

DEPLOY_BRANCH="gh-pages"
BUILD_DIR="dist"
REPO_ROOT="$(cd "$(dirname "$0")" && pwd)"
cd "$REPO_ROOT"

# ── Step 1: Compile CV ──

if command -v xelatex &>/dev/null; then
    echo "==> Compiling CV..."
    CV_DIR="CV-Overleaf"
    for tex in main.tex main_zh.tex; do
        if [ -f "$CV_DIR/$tex" ]; then
            echo "    Compiling $tex..."
            (cd "$CV_DIR" && xelatex -interaction=nonstopmode "$tex" >/dev/null 2>&1) || \
                echo "    Warning: $tex compilation failed"
        fi
    done
else
    echo "==> Skipping CV compilation (xelatex not found)"
fi

# ── Step 2: Commit source changes (including fresh CV PDFs) ──

echo "==> Checking for uncommitted changes..."
git add -A

if git diff --cached --quiet; then
    echo "    No changes to commit."
else
    if [ -n "${1:-}" ]; then
        COMMIT_MSG="$1"
    elif command -v codex &>/dev/null; then
        echo "    Generating commit message with codex..."
        CODEX_OUT=$(mktemp)
        git diff --cached --stat | \
            (cd /tmp && codex exec -m codex-spark \
                --skip-git-repo-check --ephemeral -s read-only \
                -o "$CODEX_OUT" \
                "Write ONE git commit message line, max 72 chars. No quotes. Just the message." \
                2>/dev/null) || true
        COMMIT_MSG=$(head -1 "$CODEX_OUT" 2>/dev/null | tr -d '"')
        rm -f "$CODEX_OUT"
        COMMIT_MSG="${COMMIT_MSG:-push @ $(date '+%Y-%m-%d')}"
    else
        COMMIT_MSG="push @ $(date '+%Y-%m-%d')"
    fi
    git commit -m "$COMMIT_MSG"
    echo "    Committed: $COMMIT_MSG"
fi

# ── Step 3: Push main to remote ──

CURRENT_BRANCH=$(git symbolic-ref --short HEAD 2>/dev/null || echo "detached")
echo "==> Pushing $CURRENT_BRANCH to origin..."
git push origin "$CURRENT_BRANCH"

# ── Step 4: Build site ──

echo "==> Building site..."
python generator.py

if [ ! -d "$BUILD_DIR" ]; then
    echo "Error: $BUILD_DIR not found. Build failed?"
    exit 1
fi

# ── Step 5: Deploy to gh-pages ──

echo "==> Deploying to $DEPLOY_BRANCH..."

TMPDIR=$(mktemp -d)
cp -r "$BUILD_DIR"/. "$TMPDIR"/

# Clean up any leftover worktree
git worktree remove /tmp/_deploy_worktree 2>/dev/null || rm -rf /tmp/_deploy_worktree

if git ls-remote --exit-code --heads origin "$DEPLOY_BRANCH" >/dev/null 2>&1; then
    git fetch origin "$DEPLOY_BRANCH"
    git worktree add /tmp/_deploy_worktree "$DEPLOY_BRANCH" 2>/dev/null || {
        git worktree add --detach /tmp/_deploy_worktree origin/"$DEPLOY_BRANCH"
        cd /tmp/_deploy_worktree
        git checkout -B "$DEPLOY_BRANCH" origin/"$DEPLOY_BRANCH"
    }
    cd /tmp/_deploy_worktree
    git reset --hard origin/"$DEPLOY_BRANCH" 2>/dev/null || true
else
    git worktree add --detach /tmp/_deploy_worktree 2>/dev/null || true
    cd /tmp/_deploy_worktree
    git checkout --orphan "$DEPLOY_BRANCH"
    git rm -rf . >/dev/null 2>&1 || true
fi

# Clean and copy new build
find . -maxdepth 1 ! -name '.git' ! -name '.' -exec rm -rf {} +
cp -r "$TMPDIR"/. .

git add -A
if git diff --cached --quiet; then
    echo "    No changes to deploy."
else
    DEPLOY_MSG="Deploy site $(date '+%Y-%m-%d %H:%M:%S')"
    git commit -m "$DEPLOY_MSG"
    git push origin "$DEPLOY_BRANCH"
    echo "    Deployed to $DEPLOY_BRANCH successfully."
fi

# Cleanup
cd "$REPO_ROOT"
git worktree remove /tmp/_deploy_worktree 2>/dev/null || rm -rf /tmp/_deploy_worktree
rm -rf "$TMPDIR"

echo "==> Done."
