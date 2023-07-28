#!/bin/zsh

cat /home/labex/project/logcall.py | grep "format"
cat /home/labex/project/sample.py | grep "__code__"
cat /home/labex/project/sample.py | grep "co_filename"
cat /home/labex/project/sample.py | grep "__name__"
cat ~/.python_history | grep "sample"
