#!/bin/zsh
cd /home/labex/project
git clone https://github.com/labex-labs/git-playground
cd /home/labex/project/git-playground
echo "hello,world" > test.txt
git add .
git stash save "Added test.txt"
echo "hello,labex" > test2.txt
git add .
git stash save "Added test2.txt"
