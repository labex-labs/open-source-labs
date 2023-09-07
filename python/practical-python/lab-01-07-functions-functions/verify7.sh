#!/bin/zsh
(python3 ~/project/pcost.py portfolio.csv > debug && grep "44671" debug) && echo "True"
