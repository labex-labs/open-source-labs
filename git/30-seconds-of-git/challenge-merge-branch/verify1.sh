#!/bin/zsh
cd /home/labex/project/git-playground
git branch --merged master | grep "feature-branch"
