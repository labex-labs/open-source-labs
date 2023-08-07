#!/bin/zsh
(cd /home/labex/project/git-playground && git config --list | grep "user.email=jane.doe@example.com") && (cd /home/labex/project/git-playground && git config --list | grep "user.name=Jane Doe") && echo "True"
