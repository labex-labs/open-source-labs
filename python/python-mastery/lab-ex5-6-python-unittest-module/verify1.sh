#!/bin/zsh

grep "unittest" /home/labex/project/*.py | grep -v -w "stock.py"
grep "main" /home/labex/project/*.py | grep -v -w "stock.py"
grep "assertEqual" /home/labex/project/*.py | grep -v -w "stock.py"
