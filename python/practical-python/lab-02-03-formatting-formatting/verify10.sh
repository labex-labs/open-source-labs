#!/bin/zsh
(python3 ~/project/report.py > debug3 && grep "$35." debug3) && echo "True"
