#!/bin/zsh
(cat ~/.zsh_history | grep -v grep | grep "git gc --prune=now --aggressive") && (cat ~/.zsh_history | grep -v grep | grep "cd git-playground") && echo "True"
