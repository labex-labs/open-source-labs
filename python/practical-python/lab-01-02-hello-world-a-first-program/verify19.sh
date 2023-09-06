#!/bin/zsh
(python3 ~/project/sears.py > debug && grep "NameError" debug) && echo "True"
