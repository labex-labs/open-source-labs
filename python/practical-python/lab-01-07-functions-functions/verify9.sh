#!/bin/zsh
python3 ~/project/pcost.py portfolio.csv > debug3 && cat ~/project/pcost.py | grep "import csv" && echo "True"
