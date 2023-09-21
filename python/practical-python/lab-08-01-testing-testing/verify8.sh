#!/bin/zsh
(grep -q "import simple" ~/.python_history) || (cat /home/labex/project/test_simple.py | grep -q "import simple")

