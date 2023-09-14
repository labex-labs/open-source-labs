#!/bin/zsh
(python3 ~/project/fileparse_3.7.py > debug4 && grep "{'price': '40.37', 'name': 'GE', 'shares': '95'}" debug4) && echo "True"
