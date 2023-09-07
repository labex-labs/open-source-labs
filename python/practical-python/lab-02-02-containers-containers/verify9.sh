#!/bin/zsh
(python3 ~/project/report.py > debug && grep "44671.15" debug) && echo "True"
