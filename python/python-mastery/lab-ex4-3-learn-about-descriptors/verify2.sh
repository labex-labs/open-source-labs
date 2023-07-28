#!/bin/zsh

ls /home/labex/project/descrip.py | grep "__get__"
ls /home/labex/project/descrip.py | grep "__set__"
ls /home/labex/project/descrip.py | grep "__delete__"
cat ~/.python_history | grep "del"
cat ~/.python_history | grep "__delete__"
