#!/bin/zsh
(cat /home/labex/project/report.py |grep -q "TableFormatter()")&&(cat /home/labex/project/tableformat.py |grep -q "NotImplementedError()") && echo "True"
