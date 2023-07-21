#!/bin/zsh

echo -n "" > readrides.py
cat /home/labex/project/readrides.py | grep 'open'
cat /home/labex/project/readrides.py | grep 'reader'
cat /home/labex/project/readrides.py | grep 'start'
cat /home/labex/project/readrides.py | grep 'get_traced_memory'
