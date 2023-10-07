#!/bin/zsh
(python3 ~/project/fileparse_3.9.py > debug1 && grep "Row 4" debug1) && echo "True"
