#!/bin/zsh
(cd /home/labex/project/git-playground && git config --list | less -R | grep "core.editor=vim") && echo "True"

