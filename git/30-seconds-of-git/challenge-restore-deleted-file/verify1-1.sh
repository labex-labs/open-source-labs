#!/bin/bash
(cd /home/labex/project/git-playground && cat file2.txt | grep "This is file2.") && echo "True"
