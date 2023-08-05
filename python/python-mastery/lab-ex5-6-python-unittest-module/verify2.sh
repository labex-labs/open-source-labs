#!/bin/zsh

grep -E "name.*=" /home/labex/project/*.py | grep -v -w "stock.py"
grep "cost" /home/labex/project/*.py | grep -v -w "stock.py"
grep "sell" /home/labex/project/*.py | grep -v -w "stock.py"
grep "from_row" /home/labex/project/*.py | grep -v -w "stock.py"
grep "repr" /home/labex/project/*.py | grep -v -w "stock.py"
grep "==" /home/labex/project/*.py | grep -v -w "stock.py"
