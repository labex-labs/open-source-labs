#!/bin/bash
(cd /home/labex/project/git-playground && git log | grep "Added file1.txt") && (cd /home/labex/project/git-playground && git log | grep "Added file2.txt") && echo "True"
