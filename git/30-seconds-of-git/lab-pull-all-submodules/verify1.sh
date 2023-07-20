#!/bin/zsh
(cat ~/.zsh_history | grep -v grep | grep "cd git-playground") && (cat ~/.zsh_history | grep -v grep | grep "git submodule update --recursive --remote") && echo "True"
