#!/bin/zsh

# Check if the following command is in the history:
# git push -u origin feature-branch
# or
# git push --set-upstream origin feature-branch
push_command_in_history=$(cat ~/.zsh_history | grep -v grep | grep -E "(git push -u origin feature-branch|git push --set-upstream origin feature-branch)")

# Navigate to the project directory
cd /home/labex/project/git-playground

# Check if the remote branch "feature-branch" exists
remote_branch_exists=$(git branch -r | grep "feature-branch")

# If the push command is in the history, and the remote branch doesn't exist, print "True"
if [ -n "$push_command_in_history" ] && [ -z "$remote_branch_exists" ]; then
  echo "True"
fi
