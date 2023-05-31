#!/bin/zsh
(cd /home/labex/project/git-playground && git checkout master && git fetch && git log --all | grep "(origin/master, origin/HEAD, master, feature-branch-A)") && echo "True"
