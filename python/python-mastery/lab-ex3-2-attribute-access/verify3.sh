#!/bin/zsh

ls /home/labex/project/*.py | grep -v "stock.py"
grep "def" /home/labex/project/*.py | grep -v "stock.py"
grep "print" /home/labex/project/*.py | grep -v "stock.py"
grep "join" /home/labex/project/*.py | grep -v "stock.py"
grep "getattr" /home/labex/project/*.py | grep -v "stock.py"
cat ~/.python_history | grep "stock"
cat ~/.python_history | grep "read_portfolio"
