#!/bin/zsh
(python3 ~/project/report.py > debug2 && grep "Shares" debug2 && !grep "$9.22" debug2 ) && echo "True"
