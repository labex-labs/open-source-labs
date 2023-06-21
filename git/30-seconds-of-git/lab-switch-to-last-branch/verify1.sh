#!/bin/zsh
(cd /home/labex/project/git-playgrund && git branch | less -R | grep "* master") && (cat ~/.zsh_history | grep -v grep | grep "git checkout") && echo "True"