#!/bin/zsh

ls /home/labex/project/*.py | grep -v "colreader.py"
cat ~/.python_history | grep "import"
cat ~/.python_history | grep "portfolio"
cat ~/.python_history | grep "print"
