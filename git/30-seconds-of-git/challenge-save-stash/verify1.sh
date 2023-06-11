#!/bin/zsh
(cd /home/labex/project/git-playground && git stash list | grep "On feature: My changes") && (cat ~/.zsh_history | grep -v grep | grep "git stash apply") && echo "True"
