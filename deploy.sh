#!/usr/bin/env bash
set -euo pipefail

# Smart deploy script:
#   1. Commit all source changes to main (auto-generated message)
#   2. Push main to remote
#   3. Build site and push dist/ to gh-pages branch
#
# Usage: ./deploy.sh [commit message]
#
# Prerequisites: Python deps installed, xelatex optional (for CV compilation).
# GitHub Pages should be configured to deploy from the gh-pages branch.

DEPLOY_BRANCH="gh-pages"
BUILD_DIR="dist"
REPO_ROOT="$(cd "$(dirname "$0")" && pwd)"
cd "$REPO_ROOT"

# ── Step 1: Commit source changes to main ──

echo "==> Checking for uncommitted changes..."
git add -A

if git diff --cached --quiet; then
    echo "    No changes to commit."
else
    if [ -n "${1:-}" ]; then
        # Use user-provided message
        COMMIT_MSG="$1"
    elif [ -n "${OPENROUTER_API_KEY:-}" ]; then
        # Use OpenRouter + Haiku to generate commit message from staged diff
        echo "    Generating commit message with LLM..."
        DIFF_STAT=$(git diff --cached --stat)
        COMMIT_MSG=$(curl -s "https://openrouter.ai/api/v1/chat/completions" \
            -H "Authorization: Bearer $OPENROUTER_API_KEY" \
            -H "Content-Type: application/json" \
            -d "$(jq -n --arg diff "$DIFF_STAT" '{
                model: "anthropic/claude-3.5-haiku",
                max_tokens: 60,
                messages: [{role: "user", content: ("Write a concise git commit message (one line, max 72 chars) for these changes. Output ONLY the message.\n\n" + $diff)}]
            }')" 2>/dev/null | jq -r '.choices[0].message.content // empty' 2>/dev/null | head -1 | tr -d '"')
        # Fallback if codex fails or returns empty
        COMMIT_MSG="${COMMIT_MSG:-push @ $(date '+%Y-%m-%d')}"
    else
        COMMIT_MSG="push @ $(date '+%Y-%m-%d')"
    fi
    git commit -m "$COMMIT_MSG"
    echo "    Committed: $COMMIT_MSG"
fi

# ── Step 2: Push main to remote ──

CURRENT_BRANCH=$(git symbolic-ref --short HEAD 2>/dev/null || echo "detached")
echo "==> Pushing $CURRENT_BRANCH to origin..."
git push origin "$CURRENT_BRANCH"

# ── Step 3: Build site ──

echo "==> Building site..."
python generator.py

if [ ! -d "$BUILD_DIR" ]; then
    echo "Error: $BUILD_DIR not found. Build failed?"
    exit 1
fi

# ── Step 4: Deploy to gh-pages ──

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
