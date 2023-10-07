#!/bin/zsh
(python3 ~/project/report.py > debug && grep "98000000" debug) && echo "True"
