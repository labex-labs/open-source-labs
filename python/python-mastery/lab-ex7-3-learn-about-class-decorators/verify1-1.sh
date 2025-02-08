#!/bin/zsh

cat /home/labex/project/stock.py | grep "Structure"
cat /home/labex/project/stock.py | grep "String"
cat /home/labex/project/stock.py | grep "PositiveInteger"
cat /home/labex/project/stock.py | grep "PositiveFloat"
cat /home/labex/project/stock.py | grep -E "@.*property"
