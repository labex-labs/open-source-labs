#!/bin/zsh
cd /home/labex/project
git clone https://github.com/labex-labs/git-playground
cd /home/labex/project/git-playground
echo "This is a new line" >> README.md
git stash save "This is a new line"
