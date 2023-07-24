#!/bin/zsh
 (cat ~/.zsh_history | grep -v grep | grep "git reset HEAD~1 --hard") && (cd /home/labex/project/git-playground && git checkout feature-branch && git log | grep "Add new feature to master branch") && (cd /home/labex/project/git-playground && git checkout master && ! git log | grep "Add new feature to master branch") && echo "True"
