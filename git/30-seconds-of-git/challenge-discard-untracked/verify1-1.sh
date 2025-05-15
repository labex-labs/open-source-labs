#!/bin/bash
(cd /home/labex/project/git-playground && git status | grep "nothing to commit, working tree clean") && (cd /home/labex/project/git-playground && ! ls | grep "one.txt") && (cd /home/labex/project/git-playground && ! ls | grep "two.txt") && (cd /home/labex/project/git-playground && ! ls | grep "three.txt") && echo "True"
