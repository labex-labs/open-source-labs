#!/bin/zsh
(cd /home/labex/project/git-playground | cat ~/.zsh_history | grep -v grep | grep "git rev-parse --abbrev-ref HEAD") && (cd /home/labex/project/git-playground | git rev-parse --abbrev-ref HEAD | grep "feature-branch") && echo "True"
