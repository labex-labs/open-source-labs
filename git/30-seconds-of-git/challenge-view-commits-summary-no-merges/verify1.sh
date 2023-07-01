#!/bin/zsh
(cat ~/.zsh_history | grep -v grep | grep "no-merges") && (cat ~/.zsh_history | grep -v grep | grep "git log") && echo "True"

