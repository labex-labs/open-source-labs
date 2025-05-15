#!/bin/bash
(python3 /home/labex/project/report.py /home/labex/project/portfolio.csv /home/labex/project/prices.csv > debug && grep -q "MSFT" debug && cat /home/labex/project/report.py | grep -q "Stock(") && (python3 /home/labex/project/pcost.py /home/labex/project/portfolio.csv > debug1 && grep -q "44671" debug1 && ! cat /home/labex/project/pcost.py | grep -q 's\["shares"\]') && echo "True"
