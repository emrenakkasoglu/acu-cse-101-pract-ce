#!/usr/bin/env bash
set -e

echo "============================================="
echo "  Setting up ACU CSE 101 Environment..."
echo "============================================="

# Upgrade pip and install course packages
pip install --upgrade pip
pip install -r requirements.txt -r requirements-dev.txt

# Configure safe git defaults for students
git config --global pull.rebase false
git config --global core.autocrlf input

# Set execution permissions on scripts
chmod +x scripts/*.py 2>/dev/null || true

# Ensure student starts on the 'workspace' branch, keeping 'main' pristine
if git show-ref --verify --quiet refs/heads/workspace; then
    git checkout workspace
else
    git checkout -b workspace
fi

echo "✅ ACU CSE 101 Environment Ready!"
