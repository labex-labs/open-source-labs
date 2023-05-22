#!/bin/zsh
(cat ~/.zsh_history | grep -v grep | grep "git branch -b feature-1") && (cat ~/.zsh_history | grep -v grep | grep "git branch -d feature-1") && (cd /home/labex/project/git-playground && ! git branch | grep -q "feature-1") && echo "True"
