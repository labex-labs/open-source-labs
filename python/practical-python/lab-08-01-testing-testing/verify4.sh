#!/bin/zsh
(grep -q "unittest" ~/.python_history) || (cat /home/labex/project/test_simple.py | grep -q "unittest")

