#!/bin/zsh
(cd /home/labex/project/git-playground && git branch | less -R | grep "* master") && echo "True"
