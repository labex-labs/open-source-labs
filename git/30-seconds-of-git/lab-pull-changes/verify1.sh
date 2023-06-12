#!/bin/zsh
(cat ~/.zsh_history | grep -v grep | grep "git pull origin master") && (cd /home/labex/project/git-playground && git pull origin master | grep -v grep | grep " create mode 100644 file1.txt
 create mode 100644 file2.txt") && echo "True"