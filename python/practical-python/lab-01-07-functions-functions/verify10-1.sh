#!/bin/bash
python3 ~/project/pcost.py ~/project/portfolio.csv > debug4 && grep "44671" debug4 && (cat ~/project/pcost.py | grep "portfolio.csv") && echo "True"
