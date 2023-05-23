#!/bin/zsh
(cat ~/.zsh_history | grep -v grep | grep "git push -d origin feature-branch") && (cd /home/labex/project/git-playground && ! git branch -r | grep feature-branch) && echo "True"

