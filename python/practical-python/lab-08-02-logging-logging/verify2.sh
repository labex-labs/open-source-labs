#!/bin/zsh
(cat /home/labex/project/fileparse.py | grep -q "try") || (grep -q "try" ~/.python_history)
