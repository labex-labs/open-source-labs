#!/bin/zsh
(cd /home/labex/project/git-playground && git config --list | grep "user.name=labex_git
user.email=labex_git@example.com") && (cat ~/.zsh_history | grep -v grep | grep "git config") && echo "True"
