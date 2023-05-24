#!/bin/zsh
cd /home/labex/project
git clone https://github.com/labex-labs/git-playground
cd git-playground
touch newfile.txt
git add newfile.txt
git stash save "new file added"
touch newfile.txt
git add newfile.txt
git stash save "new file added"
touch newfile.txt
git add newfile.txt
git stash save "new file added"
touch newfile.txt
git add newfile.txt
git stash save "new file added"
touch newfile.txt
git add newfile.txt
git stash save "new file added"


