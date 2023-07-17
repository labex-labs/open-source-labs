#!/bin/zsh
(cd /home/labex/project/git-playground && git checkout master && git log | grep "fix file2.txt") && (cd /home/labex/project/git-playground && git checkout feature-branch-A && git log | grep "fix file2.txt")  && echo "True"

