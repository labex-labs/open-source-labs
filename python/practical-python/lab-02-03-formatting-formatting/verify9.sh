#!/bin/zsh
(python3 ~/project/report.py > debug2  && ! cat ~/project/report.py | grep "f'$") && echo "True"
