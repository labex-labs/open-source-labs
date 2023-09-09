#!/bin/zsh
(python3 ~/project/report.py > debug && grep "print_report" report.py) && echo "True"