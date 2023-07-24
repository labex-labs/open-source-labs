#!/bin/zsh
(cd /home/labex/project/git-playground && git log origin/master | less -R | grep "Update file2.txt") && (cd /home/labex/project/git-playground && ! git log origin/master | less -R | grep "Added file2.txt") && echo "True"
