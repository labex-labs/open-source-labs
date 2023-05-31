#!/bin/zsh
(cd /home/labex/project/git-playground && git log | grep "HEAD -> master, origin/master, origin/HEAD, feature-branch-A") && echo "True"
