#!/bin/bash
(cd /home/labex/project/git-playground && git config --list | grep "merge.ff=false") && echo "True"
