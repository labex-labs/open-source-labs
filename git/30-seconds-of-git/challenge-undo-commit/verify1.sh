#!/bin/zsh
(cd /home/labex/project/git-playground && ! ls | grep "file2.txt") && (cd /home/labex/project/git-playground && git log --oneline | grep 'Revert "Added file2.txt"') && echo "True"

