#!/bin/zsh

cat ~/.python_history | grep "import"
cat ~/.python_history | grep "portfolio"
cat ~/.python_history | grep "print"
ls /home/labex/project/*.py | grep -v "colreader.py"
