#!/bin/zsh
(cat ~/.zsh_history | grep -v grep | grep "git rebase -i HEAD~3") && (cd /home/labex/project/git-playground && git branch -r | grep "my-branch") && echo "True"
    