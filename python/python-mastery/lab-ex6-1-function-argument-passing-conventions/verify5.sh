#!/bin/zsh

grep "import" /home/labex/project/*.py | grep -v "structure.py" | grep -v "teststock.py"
grep "Structure" /home/labex/project/*.py | grep -v "structure.py" | grep -v "teststock.py"
grep -E "@.*property" /home/labex/project/*.py | grep -v "structure.py" | grep -v "teststock.py"
