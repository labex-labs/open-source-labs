#!/bin/zsh
(cat ~/.zsh_history | grep -v grep | grep "git log") && (cat ~/.zsh_history | grep -v grep | grep "no-merges") && echo "True"

