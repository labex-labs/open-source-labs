#!/bin/zsh
(cat ~/.zsh_history | grep -v grep | grep "touch newfile.txt") &&(cat ~/.zsh_history | grep -v grep | grep "git add") && (cat ~/.zsh_history | grep -v grep | grep "git stash save") && (cd /home/labex/project/git-playground && ! git stash list | grep "stash@") && echo "True"
