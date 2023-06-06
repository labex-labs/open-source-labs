#!/bin/zsh
(cd /home/labex/project/git-playground && cat hello.py | grep "Hello, World") && (cat ~/.zsh_history | grep -v grep | grep "git reset HEAD~1 --hard") && (cd /home/labex/project/git-playground && git fetch origin && git log origin/rewind-commits | grep "Add hello.py file") && echo "True"

