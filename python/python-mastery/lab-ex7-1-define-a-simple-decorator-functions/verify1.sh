#!/bin/zsh

cat /home/labex/project/logcall.py | grep "print"
cat /home/labex/project/validate.py | grep "__name__"
cat /home/labex/project/validate.py | grep "return"
cat /home/labex/project/sample.py | grep -E "@.*\logged"
cat /home/labex/project/sample.py | grep "def"
cat /home/labex/project/sample.py | grep "return"
