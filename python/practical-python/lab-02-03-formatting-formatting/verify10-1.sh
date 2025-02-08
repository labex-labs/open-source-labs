#!/bin/zsh
python3 ~/project/report.py > debug3 && grep "\$9\.22" debug3 && echo "True"
