#!/bin/bash
python3 ~/project/pcost.py ~/project/portfolio.csv > debug3 && (cat ~/project/pcost.py | grep "csv.") && echo "True"
