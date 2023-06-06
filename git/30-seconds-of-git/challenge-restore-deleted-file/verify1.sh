#!/bin/zsh
(cat ~/.zsh_history | grep -v grep | grep "rm example.txt") && (cd /home/labex/project/git-playground && git status | grep --color=always -E "(new file: example.txt)") && echo "True"

