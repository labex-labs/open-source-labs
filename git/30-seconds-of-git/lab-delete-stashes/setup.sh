#!/bin/bash
cd /home/labex/project
git clone https://github.com/labex-labs/git-playground
cd /home/labex/project/git-playground
touch newfile1.txt
git add newfile1.txt
git stash save "new file added1"
touch newfile2.txt
git add newfile2.txt
git stash save "new file added2"
touch newfile3.txt
git add newfile3.txt
git stash save "new file added3"
touch newfile4.txt
git add newfile4.txt
git stash save "new file added4"
touch newfile5.txt
git add newfile5.txt
git stash save "new file added5"
