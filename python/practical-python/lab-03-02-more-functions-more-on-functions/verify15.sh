#!/bin/zsh
(python3 ~/project/fileparse_3.5.py > debug2 && grep "'price': 70.44" debug2) && echo "True"
