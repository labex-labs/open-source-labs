#!/bin/zsh
(python3 ~/project/report.py > debug && cat ~/project/report.py | grep "import fileparse") && echo "True"
