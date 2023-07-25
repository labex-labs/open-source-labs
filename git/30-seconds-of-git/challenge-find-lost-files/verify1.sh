#!/bin/zsh
(cd /home/labex/project/git-playground/.git/lost-found && ls | less -R | grep "commit") && echo "True"
