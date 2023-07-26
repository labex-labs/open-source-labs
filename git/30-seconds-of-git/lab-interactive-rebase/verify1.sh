#!/bin/zsh
(cd /home/labex/project/git-playground && ! git log | grep "Added file2.txt") && (cd /home/labex/project/git-playground && ! git log | grep "Added file1.txt") && (cd /home/labex/project/git-playground && git log | grep "Added file1.txt and file2.txt")&&echo "True"

