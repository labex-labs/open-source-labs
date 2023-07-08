#!/bin/zsh
(cat ~/.zsh_history | grep -v grep | grep "list") && (cat ~/.zsh_history | grep -v grep | grep "git stash") && echo "True"

