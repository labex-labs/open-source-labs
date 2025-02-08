#!/bin/zsh
python3 /home/labex/project/report.py /home/labex/project/portfolio.csv /home/labex/project/prices.csv txt > debug && grep -q "MSFT" debug && (! cat /home/labex/project/report.py | grep -q "tableformat\.") && echo "true"
