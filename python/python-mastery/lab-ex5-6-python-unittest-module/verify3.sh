#!/bin/zsh

grep "assertRaises" /home/labex/project/*.py | grep -v "stock.py"
grep "TypeError" /home/labex/project/*.py | grep -v "stock.py"
grep "ValueError" /home/labex/project/*.py | grep -v "stock.py"
grep "AttributeError" /home/labex/project/*.py | grep -v "stock.py"
