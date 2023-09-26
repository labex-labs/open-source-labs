#!/bin/zsh
(python3 ~/project/mortgage.py > debug5 && grep "0.00" debug5) && echo "True"
