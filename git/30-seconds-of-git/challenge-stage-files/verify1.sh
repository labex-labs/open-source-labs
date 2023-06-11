#!/bin/zsh
(cat ~/.zsh_history | grep -v grep | grep "git add") && (cat ~/.zsh_history | grep -v grep | grep "cd git-playground") && echo "True"

