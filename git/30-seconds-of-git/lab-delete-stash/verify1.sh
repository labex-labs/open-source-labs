#!/bin/zsh
(cat ~/.zsh_history | grep -v grep | grep "git stash drop") && (cat ~/.zsh_history | grep -v grep | grep "test.txt") && (cd /home/labex/project/git-playground && ! git stash list | grep "my stash") && echo "True"
