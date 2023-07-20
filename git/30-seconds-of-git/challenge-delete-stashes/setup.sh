#!/bin/zsh
cd /home/labex/project
git clone https://github.com/labex-labs/git-playground
cd git-playground
touch newfile.txt
git add newfile.txt
git stash save "new file added1"
touch newfile.txt
git add newfile.txt
git stash save "new file added2"
touch newfile.txt
git add newfile.txt
git stash save "new file added3"
touch newfile.txt
git add newfile.txt
git stash save "new file added4"
touch newfile.txt
git add newfile.txt
git stash save "new file added5"


