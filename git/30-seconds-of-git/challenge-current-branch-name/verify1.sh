#!/bin/zsh
cd /home/labex/project/git-playground
command=$(history | tail -n 3 | head -n 1);
[ "${command#git rev-parse --abbrev-ref HEAD}" != "$command" ] && [ "$(git rev-parse --abbrev-ref HEAD)" = "feature-branch" ] && echo "True"
