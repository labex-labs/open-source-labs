#!/bin/bash
cd /home/labex/project
git clone https://github.com/labex-labs/git-playground.git
cd /home/labex/project/git-playground
git checkout -b feature-branch
echo "some changes" >> README.md
git stash save "my changes"
