#!/bin/zsh
cd /home/labex/project/git-playground
git status |& grep -qi "error\|conflict"
