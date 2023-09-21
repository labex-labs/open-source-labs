#!/bin/zsh
(cat /home/labex/project/main.py | grep -q "__main__") || (grep -q "__main__" ~/.python_history)
