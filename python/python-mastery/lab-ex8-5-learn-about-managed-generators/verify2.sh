#!/bin/zsh

grep "socket" /home/labex/project/*.py | grep -v "multitask.py"
grep "select" /home/labex/project/*.py | grep -v "multitask.py"
grep "collections" /home/labex/project/*.py | grep -v "multitask.py"
grep "any" /home/labex/project/*.py | grep -v "multitask.py"
grep "except" /home/labex/project/*.py | grep -v "multitask.py"
grep "RuntimeError" /home/labex/project/*.py | grep -v "multitask.py"
grep "send" /home/labex/project/*.py | grep -v "multitask.py"
grep "__main__" /home/labex/project/*.py | grep -v "multitask.py"
