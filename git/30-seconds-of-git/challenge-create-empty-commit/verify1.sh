#!/bin/zsh
(cd /home/labex/project/git-playground && git diff-tree --quiet HEAD~1 HEAD) && (cd /home/labex/project/git-playground && git log --name-status HEAD^. .HEAD | grep -q "Empty commit") && echo "True"
