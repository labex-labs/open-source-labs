#!/bin/zsh
(cd /home/labex/project/git-playground && git status | grep "On branch master") && (cd /home/labex/project/my-project && git status | grep "On branch master") && echo "True"

