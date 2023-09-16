#!/bin/zsh
(python3 ~/project/pcost.py /home/labex/project/portfolio.csv > debug && grep "4467" debug) && (python3 ~/project/report.py /home/labex/project/portfolio.csv /home/labex/project/prices.csv > debug1 && grep "Shares" debug1) && echo "True"
