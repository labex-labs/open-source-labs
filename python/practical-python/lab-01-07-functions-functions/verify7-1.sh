#!/bin/bash
python3 ~/project/pcost.py ~/project/portfolio.csv > debug && grep "44671.15" debug && echo "True"
