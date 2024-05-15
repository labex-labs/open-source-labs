#!/bin/zsh
(cat /home/labex/project/report.py | grep -q "HTMLTableFormatter()") && (cat /home/labex/project/tableformat.py | grep -q "HTMLTableFormatter") && echo "True"
