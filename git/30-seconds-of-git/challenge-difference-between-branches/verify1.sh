#!/bin/zsh
(cat ~/.zsh_history | grep -v grep | grep "git diff feature-1..feature-2") && (cd /home/labex/project/git-playground && git diff feature-1..feature-2 | grep "README.md") && (cd /home/labex/project/git-playground && git diff feature-1..feature-2 | grep "index.html") && echo "True"
