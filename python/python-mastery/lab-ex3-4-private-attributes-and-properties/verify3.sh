#!/bin/zsh

cat /home/labex/project/stock.py | grep -E '@.*shares.*\..*setter'
cat /home/labex/project/stock.py | grep -E '@.*price.*\..*setter'
