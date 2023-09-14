#!/bin/zsh
(python3 ~/project/fileparse_3.9.py > debug3 && grep "raise RuntimeError" debug3) && echo "True"
