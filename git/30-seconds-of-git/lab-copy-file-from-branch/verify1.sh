#!/bin/zsh
(cd /home/labex/project/git-playground && git checkout feature-1 && cat hello.txt | grep "hello,world") && (cd /home/labex/project/git-playground && git checkout feature-2 && cat hello.txt | grep "hello,world") && echo "True"

