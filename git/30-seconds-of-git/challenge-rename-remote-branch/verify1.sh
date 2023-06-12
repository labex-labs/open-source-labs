#!/bin/zsh
(cat ~/.zsh_history | grep -v grep | grep "git branch -m feature-1 new-feature-1") && (cat ~/.zsh_history | grep -v grep | grep "git push origin --delete feature-1") && (cat ~/.zsh_history | grep -v grep | grep "git push origin -u new-feature-1") && (cd /home/labex/project/git-playground && git branch -a | grep "remotes/origin/new-feature-1") && echo "True"


