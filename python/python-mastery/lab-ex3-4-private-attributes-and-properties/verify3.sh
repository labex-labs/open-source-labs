#!/bin/zsh

cat ~/.python_history | grep "TypeError"
cat ~/.python_history | grep "ValueError"
cat /home/labex/project/stock.py | grep -E '@.*shares.*\..*setter'
cat /home/labex/project/stock.py | grep -E '@.*price.*\..*setter'
