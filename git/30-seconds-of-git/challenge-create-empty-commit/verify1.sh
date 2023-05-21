#!/bin/zsh
(cd /home/labex/project/git-playground && git diff-tree --quiet HEAD~1 HEAD) && echo "True" || echo ""
  