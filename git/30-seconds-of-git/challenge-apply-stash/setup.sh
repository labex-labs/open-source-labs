#!/bin/zsh
git clone https://github.com/labex-labs/git-playground.git /home/labex/project/
cd /home/labex/project/
git checkout -b feature-branch
echo "some changes" >> README.md
git stash save "my changes"
git checkout master
echo "some bug fixes" >> README.md
git stash save "some bug fixes"
git checkout feature-branch
git add .


