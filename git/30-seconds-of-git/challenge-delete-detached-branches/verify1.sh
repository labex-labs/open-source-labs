#!/bin/zsh

# Navigate to the project directory
cd /home/labex/project/git-playground

# Check if the remote branch "remotes/origin/feature-branch" exists
remote_branch_exists=$(git branch -a | grep "remotes/origin/feature-branch")

# Check if the local branch "feature-branch" exists
local_branch_exists=$(git branch | grep "feature-branch")

# Check if any of the following commands related to "feature-branch" are in the history
branch_command_in_history=$(cat ~/.zsh_history | grep -v grep | grep -E "(git checkout -b feature-branch|git checkout feature-branch|git branch feature-branch)")

# If the remote and local branches don't exist, and a relevant command is in the history, print "True"
if [ -z "$remote_branch_exists" ] \
  && [ -z "$local_branch_exists" ] \
  && [ -n "$branch_command_in_history" ]; then
  echo "True"
fi
