#!/bin/zsh
(cd /home/labex/project/git-playground && git status | less -R | grep 'Untracked files:
  (use "git add <file>..." to include in what will be committed)
        newfile.txt"') && echo "true"
