#!/bin/zsh
grep -q "\-^" ~/.python_history && python3 ~/project/report.py > debug && cat ~/project/report.py | grep -q "portfolio_report" && echo "True"
