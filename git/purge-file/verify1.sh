#!/bin/zsh
cat ~/.zsh_history | grep -v grep | grep "git filter-branch"
cat ~/.zsh_history | grep -v grep | grep "git rm"
cat ~/.zsh_history | grep -v grep | grep "git push"
