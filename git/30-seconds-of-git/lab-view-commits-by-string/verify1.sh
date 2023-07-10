#!/bin/zsh
(cat ~/.zsh_history | grep -v grep | grep "Git Playground") && (cat ~/.zsh_history | grep -v grep | grep "git log") && echo "True"

