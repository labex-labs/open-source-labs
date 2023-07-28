#!/bin/zsh

cat /home/labex/project/validate.py | grep "__init_subclass__"
cat /home/labex/project/structure.py | grep "__new__"
cat /home/labex/project/structure.py | grep "__prepare__"
cat /home/labex/project/structure.py | grep "staticmethod"
grep -v "validate" /home/labex/project/stock.py
