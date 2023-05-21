#!/bin/zsh
cd /home/labex/project/git-playground
(cat ~/.zsh_history | grep -v grep | grep "git rev-parse --abbrev-ref HEAD") && ($(git rev-parse --abbrev-ref HEAD)" = "feature-branch") && echo "True"
