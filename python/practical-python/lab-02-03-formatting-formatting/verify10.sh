#!/bin/zsh
(python3 ~/project/report.py > debug3 && cat ~/project/report.py | less -R | grep "f'$") && echo "True"
