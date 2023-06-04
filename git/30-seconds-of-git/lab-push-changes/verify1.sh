#!/bin/zsh
(cd /home/labex/project/git-playground && git log -r | grep "Added new feature") && echo "True"