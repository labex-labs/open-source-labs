#!/bin/zsh
(cd /home/labex/project/git-playgrund && git branch | less -R | grep "* master") && echo "True"
