#!/bin/bash
python3 ~/project/pcost.py /home/labex/project/portfolio.csv > debug && grep -q "44671" debug && cat ~/project/pcost.py | grep -q "__main__" && python3 ~/project/report.py /home/labex/project/portfolio.csv /home/labex/project/prices.csv > debug1 && grep -q "MSFT" debug1 && cat ~/project/report.py | grep -q "__main__" && echo "true"
