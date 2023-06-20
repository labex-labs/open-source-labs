#!/bin/zsh
(cd /home/labex/project/git-playground && git stash list | grep "On feature: My changes") && (cd /home/labex/project/git-playground && git status | less -R | grep "modified:   README.md") && echo "True"
