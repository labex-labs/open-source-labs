#!/bin/bash
(cd /home/labex/project/git-playground && git diff | less -R | grep "# git-playground
 Git Playground
+some changes") && echo "True"
