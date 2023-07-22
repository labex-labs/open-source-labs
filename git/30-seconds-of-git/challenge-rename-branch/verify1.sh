#!/bin/zsh
(cd /home/labex/project/git-playground && ! git branch | grep "old-branch") && (cd /home/labex/project/git-playground && git branch | grep "new-branch") && echo "True"
