#!/bin/zsh

cat /home/labex/project/stock.py | grep "property"
cat /home/labex/project/stock.py | grep -E "@.*\..*setter"
