#!/bin/zsh
cat ~/.zsh_history | grep -v grep | grep "git push"
cat ~/.zsh_history | grep -v grep | grep "git checkout"
cat ~/.zsh_history | grep -v grep | grep "git branch"
