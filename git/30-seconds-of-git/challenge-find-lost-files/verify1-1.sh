#!/bin/bash
(cd /home/labex/project/git-playground/.git/lost-found && ls | less -R | grep "commit") && echo "True"
