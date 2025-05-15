#!/bin/bash
cd /home/labex/project
git clone https://github.com/labex-labs/git-playground
cd git-playground
echo "hello" > test.txt
git add .
git stash save "my stash"
