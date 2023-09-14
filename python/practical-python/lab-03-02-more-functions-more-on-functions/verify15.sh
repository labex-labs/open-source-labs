#!/bin/zsh
(python3 ~/project/fileparse_3.5.py > debug1 && grep "95}" debug1) && echo "True"
