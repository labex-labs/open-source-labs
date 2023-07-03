#!/bin/zsh
(cd /home/labex/project/git-playground && git log | grep "fix file2.txt") && (cat ~/.zsh_history | grep -v grep | grep "git merge feature-branch-A") && echo "True"
