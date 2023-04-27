#!/bin/zsh
cat ~/.zsh_history | grep -v grep | grep "git push"
cat ~/.zsh_history | grep -v grep | grep "git pull"
cat ~/.zsh_history | grep -v grep | grep "git checkout"
cat ~/.zsh_history | grep -v grep | grep "git rebase"
