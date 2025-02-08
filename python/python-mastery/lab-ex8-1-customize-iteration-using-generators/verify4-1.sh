#!/bin/zsh

ls /home/labex/project/*.csv | grep -v "dowstocks.csv"
grep "open" /home/labex/project/*.py | grep -v "structure.py" | grep -v "stocksim.py" | grep -v "validate.py" | grep -v "stock.py"
grep "seek" /home/labex/project/*.py | grep -v "structure.py" | grep -v "stocksim.py" | grep -v "validate.py" | grep -v "stock.py"
grep "SEEK_END" /home/labex/project/*.py | grep -v "structure.py" | grep -v "stocksim.py" | grep -v "validate.py" | grep -v "stock.py"
grep "readline" /home/labex/project/*.py | grep -v "structure.py" | grep -v "stocksim.py" | grep -v "validate.py" | grep -v "stock.py"
grep "yield" /home/labex/project/*.py | grep -v "structure.py" | grep -v "stocksim.py" | grep -v "validate.py" | grep -v "stock.py"
