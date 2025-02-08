#!/bin/zsh
(python3 ~/project/fileparse_3.10.py > debug && grep "MSFT" debug) && echo "True"
