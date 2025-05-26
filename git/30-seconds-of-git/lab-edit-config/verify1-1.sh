#!/bin/bash
(cd /home/labex/project/git-playground && git config --list | grep "user.name=labex_git" && git config --list | grep "user.email=labex_git@example.com") && echo "True"
