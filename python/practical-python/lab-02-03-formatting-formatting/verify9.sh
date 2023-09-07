#!/bin/zsh
(python3 ~/project/report.py > debug2 && grep "Shares" debug2) && echo "True"
