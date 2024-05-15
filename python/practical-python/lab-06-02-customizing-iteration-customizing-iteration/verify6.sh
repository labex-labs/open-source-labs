#!/bin/zsh
(cat /home/labex/project/follow.py | grep -q "import report") && echo "true"
