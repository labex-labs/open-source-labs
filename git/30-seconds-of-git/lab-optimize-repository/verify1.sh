#!/bin/zsh
(cat ~/.zsh_history | grep -v grep | grep "git gc") && (cat ~/.zsh_history | grep -v grep | grep "aggressive") && (cat ~/.zsh_history | grep -v grep | grep "prune") && echo "True"



