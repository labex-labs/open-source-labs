#!/bin/zsh
(cat ~/.zsh_history | grep -v grep | grep 'git merge --no-ff -m "Merge feature-branch" feature-branch') && (cd /home/labex/project/git-playground && git log | grep "Merge feature-branch") && echo "True"
