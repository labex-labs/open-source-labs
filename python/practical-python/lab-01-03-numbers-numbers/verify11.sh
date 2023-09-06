#!/bin/zsh
(python3 ~/project/mortgage.py > debug5 && grep " 0 " debug5) && echo "True"
