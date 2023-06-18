#!/bin/zsh
(cat ~/.zsh_history | grep -v grep | grep "rm file2.txt") && (cd /home/labex/project/git-playground && ll | grep "file2.txt") && echo "True"
