#!/bin/zsh
(cat ~/.zsh_history | grep -v grep | grep "git branch -m old-branch new-branch") && (cd /home/labex/project/git-playground && git branch | grep "new-branch") && echo "True"
