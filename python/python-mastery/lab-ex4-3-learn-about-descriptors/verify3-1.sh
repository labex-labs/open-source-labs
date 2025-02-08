#!/bin/zsh

cat /home/labex/project/validate.py | grep "__set__"
cat /home/labex/project/stock.py | grep "String"
cat /home/labex/project/stock.py | grep "PositiveInteger"
cat /home/labex/project/stock.py | grep "PositiveFloat"
