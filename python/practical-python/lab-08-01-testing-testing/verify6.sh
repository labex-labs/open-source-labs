#!/bin/zsh
(grep -q "unittest.main" ~/.python_history) || (cat /home/labex/project/test_simple.py | grep -q "unittest.main")

