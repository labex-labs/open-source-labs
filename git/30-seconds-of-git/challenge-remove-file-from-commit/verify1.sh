#!/bin/zsh
 (cd /home/labex/project/git-playground && git show HEAD | less -R | grep "add git-playground.txt") && (cd /home/labex/project/git-playground && ! git show HEAD | less -R | grep "file1.txt") && echo "True"

