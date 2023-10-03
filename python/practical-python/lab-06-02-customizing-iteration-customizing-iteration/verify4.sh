#!/bin/zsh
(cat /home/labex/project/stocklog.csv | grep -q "AAPL") && python3 /home/labex/project/follow.py && echo "true"
