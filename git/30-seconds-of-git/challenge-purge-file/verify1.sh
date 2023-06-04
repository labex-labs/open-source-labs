#!/bin/zsh
(cat ~/.zsh_history | grep -v grep | grep 'git filter-branch --force --index-filter "git rm --cached --ignore-unmatch file1.txt" --prune-empty --tag-name-filter cat -- --all')&&(cd /home/labex/project/git-playground && ! git log -r | grep "file1.txt") && echo "True"
