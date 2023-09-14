#!/bin/zsh
(python3 ~/project/fileparse_3.4.py > debug1 && grep "'100'}]" debug1) && echo "True"
