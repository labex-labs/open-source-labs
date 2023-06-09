#!/bin/zsh
(cat ~/.zsh_history | grep -v grep | grep "git branch --sort=-committerdate") && (cat ~/.zsh_history | grep -v grep | grep "cd git-playground") && echo "True"

