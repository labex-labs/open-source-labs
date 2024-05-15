#!/bin/zsh
(cd /home/labex/project/git-playground && git checkout feature && git log | grep "Added hello.txt") && (cd /home/labex/project/git-playground && git checkout master && ! git log | grep "Added hello.txt") && echo "True"
