#!/bin/zsh
(cd /home/labex/project/git-playground && ! git log origin/rewind-commits --oneline | grep "Added file2.txt") && echo "True"
