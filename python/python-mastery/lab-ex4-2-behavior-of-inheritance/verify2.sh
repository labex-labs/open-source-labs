#!/bin/zsh

ls /home/labex/project/*.py | grep -v "stock.py"
grep "classmethod" /home/labex/project/*.py | grep -v "stock.py"
grep "isinstance" /home/labex/project/*.py | grep -v "stock.py"
grep "super" /home/labex/project/*.py | grep -v "stock.py"
grep "raise" /home/labex/project/*.py | grep -v "stock.py"
grep "int" /home/labex/project/*.py | grep -v "stock.py"
grep "float" /home/labex/project/*.py | grep -v "stock.py"
grep "str" /home/labex/project/*.py | grep -v "stock.py"
cat ~/.python_history | grep "raise"
