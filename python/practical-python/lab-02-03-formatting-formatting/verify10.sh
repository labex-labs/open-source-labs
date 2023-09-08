#!/bin/zsh
(python3 ~/project/report.py > debug3 && cat ~/project/report.py | grep "f'$") && echo "True"
