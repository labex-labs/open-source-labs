#!/bin/zsh
python3 ~/project/report.py > debug2 && grep -q "\-----" debug2 && echo "True"