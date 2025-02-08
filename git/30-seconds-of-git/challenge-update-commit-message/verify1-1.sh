#!/bin/zsh
(cd /home/labex/project/git-playground && git log --oneline | grep "Fix the network bug") && (cd /home/labex/project/git-playground && ! git log --oneline | grep "Added file2.txt") && echo "True"
