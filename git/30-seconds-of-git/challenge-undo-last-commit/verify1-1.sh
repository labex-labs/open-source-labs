#!/bin/bash
(cd /home/labex/project/git-playground && ! ls | grep "file2.txt") && echo "True"
