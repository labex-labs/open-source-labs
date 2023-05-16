#!/bin/zsh
cd /home/labex/project/git-playground/master
git status |& grep -q "error\|conflict"
