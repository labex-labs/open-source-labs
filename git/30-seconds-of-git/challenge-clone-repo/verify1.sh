#!/bin/zsh
(cd /home/labex/project/my-project && git status | grep "On branch master") && echo "True"


