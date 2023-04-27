#!/bin/zsh
cat ~/.zsh_history | grep -v grep | grep "git config"
cat ~/.zsh_history | grep -v grep | grep "git checkout"
cat ~/.zsh_history | grep -v grep | grep "git merge"
