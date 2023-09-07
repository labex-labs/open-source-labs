#!/bin/zsh
python3 ~/project/pcost.py ~/project/portfolio.csv > debug4 && grep "44671" debug4 && echo "True"
