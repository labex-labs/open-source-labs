#!/bin/zsh
git clone https://github.com/labex-labs/git-playground.git
cd git-playground
git checkout -b feature-branch
echo "some changes" >> README.md
git stash save "my changes"
git checkout master
echo "some bug fixes" >> README.md
git checkout feature-branch


