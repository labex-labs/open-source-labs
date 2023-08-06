#!/bin/zsh
(cat ~/.zsh_history | grep -v grep | grep "git gc") && (cat ~/.zsh_history | grep -v grep | grep "cd git-playground") && echo "True"

