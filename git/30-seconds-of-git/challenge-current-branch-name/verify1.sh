#!/bin/zsh
command=$(history | tail -n 2 | head -n 1);
[ "${command#git rev-parse --abbrev-ref HEAD}" != "$command" ] && [ "$(git rev-parse --abbrev-ref HEAD)" = "feature-branch" ] && echo "True"