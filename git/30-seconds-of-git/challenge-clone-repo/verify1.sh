#!/bin/zsh
(cd /home/labex/project/my-project && git status | grep "On branch master" >/dev/null) && echo "True"


