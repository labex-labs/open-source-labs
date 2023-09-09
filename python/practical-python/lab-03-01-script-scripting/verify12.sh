#!/bin/zsh
(python3 ~/project/report.py > debug && grep "portfolio_report" report.py) && echo "True"