#!/bin/zsh
(cat ~/.zsh_history | grep -v grep | grep 'git stash save "My changes"') && (cd /home/labex/project/git-playground && git stash apply | grep "error: Your local changes to the following files would be overwritten by merge:
        README.md") && echo "True"
