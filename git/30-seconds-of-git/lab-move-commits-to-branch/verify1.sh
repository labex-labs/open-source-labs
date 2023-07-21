#!/bin/zsh
(cd /home/labex/project/git-playground && git checkout feature-branch && git log | grep "Added hello.txt") && (cd /home/labex/project/git-playground && git checkout master && ! git log | grep "Added hello.txt") echo "True"

