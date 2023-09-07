#!/bin/zsh
python3 ~/project/pcost.py portfolio.csv > debug && grep "44671.15" debug && echo "True"
