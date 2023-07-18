#!/bin/zsh
(cd /home/labex/project/git-playground && ! git log --oneline | grep "Added file2.txt") && (cd /home/labex/project/git-playground && ! git log --oneline | grep "Added file1.txt") && echo "True"
