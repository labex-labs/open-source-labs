#!/bin/zsh
(python3 ~/project/pcost.py /home/labex/project/portfolio.csv > debug && grep "44671" debug) && echo "True"
