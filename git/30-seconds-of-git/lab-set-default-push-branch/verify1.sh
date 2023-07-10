#!/bin/zsh
(cd /home/labex/project/git-playground && git config push.default | grep "current") && (cd /home/labex/project/git-playground && git branch -vv --no-color | grep "origin/my-branch") && echo "True"
