#!/bin/zsh
(cat ~/.zsh_history | grep -v grep | grep "git checkout") && (cat ~/.zsh_history | grep -v grep | grep "rm example.txt") && (cd /home/labex/project/git-playground && git status | grep "new file: example.txt") && echo "True"

