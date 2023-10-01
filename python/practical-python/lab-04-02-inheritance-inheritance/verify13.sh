#!/bin/zsh
(cat /home/labex/project/report.py |grep -q "CSVTableFormatter()")&&(cat /home/labex/project/tableformat.py |grep -q "CSVTableFormatter") && echo "True"
