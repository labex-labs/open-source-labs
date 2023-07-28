#!/bin/zsh

grep -E "name.*=" /home/labex/project/*.py | grep -v "stock.py"
grep "cost" /home/labex/project/*.py | grep -v "stock.py"
grep "sell" /home/labex/project/*.py | grep -v "stock.py"
grep "from_row" /home/labex/project/*.py | grep -v "stock.py"
grep "repr" /home/labex/project/*.py | grep -v "stock.py"
grep "==" /home/labex/project/*.py | grep -v "stock.py"
