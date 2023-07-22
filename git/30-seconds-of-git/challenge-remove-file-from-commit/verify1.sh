#!/bin/zsh
(cd /home/labex/project/git-playground && ! git show HEAD | less -R | grep "diff") &&(cd /home/labex/project/git-playground && git show HEAD | less -R | grep "Added file2.txt") && echo "True"

