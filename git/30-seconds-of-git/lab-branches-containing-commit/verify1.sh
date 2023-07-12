#!/bin/zsh
(cat ~/.zsh_history | grep -v grep | grep "git branch") && (cat ~/.zsh_history | grep -v grep | grep "contain") && echo "True"

