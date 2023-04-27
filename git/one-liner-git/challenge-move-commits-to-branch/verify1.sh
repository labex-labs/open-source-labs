#!/bin/zsh
cat ~/.zsh_history | grep -v grep | grep "git add"
cat ~/.zsh_history | grep -v grep | grep "git branch"
cat ~/.zsh_history | grep -v grep | grep "git reset"
cat ~/.zsh_history | grep -v grep | grep "git checkout"
cat ~/.zsh_history | grep -v grep | grep "git commit"
