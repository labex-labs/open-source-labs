#!/bin/zsh
(python3 ~/project/pcost.py > debug1 && grep "32.20" debug1) && echo "True"