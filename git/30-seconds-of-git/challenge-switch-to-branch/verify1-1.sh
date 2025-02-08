#!/bin/zsh
(cd /home/labex/project/git-playground && git branch | less -R | grep "* feature-1") && echo "True"
