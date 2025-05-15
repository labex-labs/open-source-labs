#!/bin/bash
(cd /home/labex/project/git-playground && git show HEAD | less -R | grep " # git-playground
 Git Playground
+New content") && echo "True"
