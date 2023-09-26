#!/bin/zsh
(python3 ~/project/mortgage.py > debug1 && grep "1871" debug1) && echo "True"
