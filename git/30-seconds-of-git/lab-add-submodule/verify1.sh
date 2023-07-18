#!/bin/zsh
(cd /home/labex/project/my-project && git submodule status | grep git-playground) && echo "True"

