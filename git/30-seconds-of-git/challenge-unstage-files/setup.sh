#!/bin/zsh
cd /home/labex/project
git clone https://github.com/labex-labs/git-playground.git
cd /home/labex/project/git-playground
touch newfile.txt
echo "hello,world" > README.md
git add .
