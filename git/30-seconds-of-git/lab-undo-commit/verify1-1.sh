#!/bin/bash
(cd /home/labex/project/git-playground && ! ls | grep "file1.txt") && (cd /home/labex/project/git-playground && git log --oneline | grep 'Revert "Added file1.txt"') && echo "True"
