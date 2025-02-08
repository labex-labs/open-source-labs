#!/bin/zsh
(cd /home/labex/project/git-playground && git status | grep "nothing to commit, working tree clean") && (cd /home/labex/project/git-playground && ! ls | grep "new-file.txt") && echo "True"
