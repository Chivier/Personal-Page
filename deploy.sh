#!/usr/bin/env bash
set -euo pipefail

# Local deploy script: build site and push dist/ to gh-pages branch.
# Usage: ./deploy.sh [commit message]
#
# Prerequisites: Python deps installed, xelatex optional (for CV compilation).
# GitHub Pages should be configured to deploy from the gh-pages branch.

DEPLOY_BRANCH="gh-pages"
BUILD_DIR="dist"
COMMIT_MSG="${1:-Deploy site $(date '+%Y-%m-%d %H:%M:%S')}"

echo "==> Building site..."
python generator.py

if [ ! -d "$BUILD_DIR" ]; then
    echo "Error: $BUILD_DIR not found. Build failed?"
    exit 1
fi

# Save current branch
CURRENT_BRANCH=$(git symbolic-ref --short HEAD 2>/dev/null || echo "detached")

echo "==> Deploying to $DEPLOY_BRANCH..."

# Use a temporary directory to avoid messing with working tree
TMPDIR=$(mktemp -d)
cp -r "$BUILD_DIR"/. "$TMPDIR"/

# Check if gh-pages branch exists on remote
if git ls-remote --exit-code --heads origin "$DEPLOY_BRANCH" >/dev/null 2>&1; then
    git fetch origin "$DEPLOY_BRANCH"
    git worktree add --detach /tmp/_deploy_worktree origin/"$DEPLOY_BRANCH" 2>/dev/null || true
    cd /tmp/_deploy_worktree
    git checkout -B "$DEPLOY_BRANCH" origin/"$DEPLOY_BRANCH"
else
    # Create orphan branch
    git worktree add --detach /tmp/_deploy_worktree 2>/dev/null || true
    cd /tmp/_deploy_worktree
    git checkout --orphan "$DEPLOY_BRANCH"
    git rm -rf . >/dev/null 2>&1 || true
fi

# Clean and copy new build
find . -maxdepth 1 ! -name '.git' ! -name '.' -exec rm -rf {} +
cp -r "$TMPDIR"/. .

# Commit and push
git add -A
if git diff --cached --quiet; then
    echo "==> No changes to deploy."
else
    git commit -m "$COMMIT_MSG"
    git push origin "$DEPLOY_BRANCH"
    echo "==> Deployed to $DEPLOY_BRANCH successfully."
fi

# Cleanup
cd -
git worktree remove /tmp/_deploy_worktree 2>/dev/null || rm -rf /tmp/_deploy_worktree
rm -rf "$TMPDIR"

echo "==> Done. GitHub Pages should serve from branch: $DEPLOY_BRANCH"
