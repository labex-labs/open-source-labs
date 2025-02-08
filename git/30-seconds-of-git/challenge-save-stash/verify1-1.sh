#!/bin/zsh
(cd /home/labex/project/git-playground && git stash list | grep "On feature: My changes") && echo "True"
