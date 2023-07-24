#!/bin/zsh
(cd /home/labex/project/git-playground && git config push.default | grep "current") && (cd /home/labex/project/git-playground && git branch -a | less -R | grep "origin/my-branch") && echo "True"

