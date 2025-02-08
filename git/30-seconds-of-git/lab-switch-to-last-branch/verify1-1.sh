#!/bin/zsh
(cd /home/labex/project/git-playground && git branch | less -R | grep "* master") && (cat ~/.zsh_history | grep -v grep | grep "git checkout") && echo "True"
