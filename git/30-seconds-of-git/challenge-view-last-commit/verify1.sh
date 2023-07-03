#!/bin/zsh
(cat ~/.zsh_history | grep -v grep | grep "l") && (cat ~/.zsh_history | grep -v grep | grep "git log") && echo "True"
