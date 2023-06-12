#!/bin/zsh
(cat ~/.zsh_history | grep -v grep | grep "git rebase feature-branch") && (cd /home/labex/project/git-playground && git checkout master && git log -r | grep "Added some changes to README.md") && echo "True"
