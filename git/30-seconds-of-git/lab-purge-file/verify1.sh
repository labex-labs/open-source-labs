#!/bin/zsh
(cd /home/labex/project/git-playground && ! git log --remotes | grep "file1.txt") && echo "True"