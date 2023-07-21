#!/bin/zsh
(((cat ~/.zsh_history | grep -v grep | grep "git push -u") && (cat ~/.zsh_history | grep -v grep | grep "origin") && (cat ~/.zsh_history | grep -v grep | grep "feature-branch")) || (cat ~/.zsh_history | grep -v grep | grep "git push --set-upstream origin feature-branch")) && (cd /home/labex/project/git-playground && ! git branch -r | grep feature-branch) && echo "True"

