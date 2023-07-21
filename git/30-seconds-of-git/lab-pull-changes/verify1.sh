#!/bin/zsh
(cd /home/labex/project/git-playground && ls | grep "file2.txt")&& (cd /home/labex/project/git-playground && ls | grep "file1.txt") && echo "True"
