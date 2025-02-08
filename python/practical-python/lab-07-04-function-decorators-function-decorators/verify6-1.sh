#!/bin/zsh
python3 /home/labex/project/timethis.py > debug && grep -q "countdown" debug && echo "true"
