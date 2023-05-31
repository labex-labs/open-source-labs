#!/bin/zsh
(cat ~/.zsh_history | grep -v grep | grep "git cherry-pick master") && (cd /home/labex/project/git-playground && git checkout feature-branch && git log | grep "Add new feature to master branch") && echo "True"

