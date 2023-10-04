#!/bin/zsh
python3 /home/labex/project/porty-app/print-report.py /home/labex/project/porty-app/portfolio.csv /home/labex/project/porty-app/prices.csv txt > debug && grep "MSFT" debug