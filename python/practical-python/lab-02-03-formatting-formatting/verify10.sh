#!/bin/zsh
(python3 ~/project/report.py > debug3 && grep "$" debug3) && echo "True"
