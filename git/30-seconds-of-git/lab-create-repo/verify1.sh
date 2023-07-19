#!/bin/zsh
(cd /home/labex/project/my_project && git status | grep "On branch") && (cd /home/labex/project/git-playground && git status | grep "On branch") && echo "True"

