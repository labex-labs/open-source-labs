#!/bin/zsh
(cat ~/.zsh_history | grep -v grep | grep "git log") && (cat ~/.zsh_history | grep -v grep | grep "graph") && echo "TRUE"
