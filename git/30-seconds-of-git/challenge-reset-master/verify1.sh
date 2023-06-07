#!/bin/zsh
(cat ~/.zsh_history | grep -v grep | grep "git fetch origin") && (cat ~/.zsh_history | grep -v grep | grep "git reset --hard origin/master") && (cd /home/labex/project/git-playground && git status | grep "nothing to commit, working tree clean") && echo "True"


