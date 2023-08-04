#!/bin/zsh

cat /home/labex/project/validate.py | grep "__set_name__"
cat /home/labex/project/stock.py | grep -E "String.*\(\s*"
cat /home/labex/project/stock.py | grep -E "PositiveInteger.*\(\s*"
cat /home/labex/project/stock.py | grep -E "PositiveFloat.*\(\s*"
