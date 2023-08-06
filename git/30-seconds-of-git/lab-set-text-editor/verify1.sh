#!/bin/zsh
(cd /home/labex/project/git-playground && git config --list | grep "core.editor=vim") && (cd /home/labex/project/git-playground && git log | grep "Update hello.txt") && echo "True"

