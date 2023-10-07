#!/bin/zsh
(python3 ~/project/report.py > debug && cat ~/project/report.py | grep -q "def print_report") && echo "True"