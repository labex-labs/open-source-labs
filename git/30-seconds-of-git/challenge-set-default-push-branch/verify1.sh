#!/bin/zsh
(cd /home/labex/project/git-playground && git config push.default | grep "current") && (cd /home/labex/project/git-playground && git log origin/my-branch | grep "Add hello.txt") && echo "True"
