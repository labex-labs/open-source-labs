#!/bin/zsh
(cat /home/labex/project/report.py |grep -q "dict(zip") &&(python3 ~/project/report.py > debug1 && grep "32.2" debug1) && echo "True"