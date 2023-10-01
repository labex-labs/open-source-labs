#!/bin/zsh
(cat /home/labex/project/report.py |grep -q "fmt='txt'")&& echo "True"
