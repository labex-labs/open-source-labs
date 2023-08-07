#!/bin/zsh
python3 ~/project/art.py 10 20 | awk '{print length}' | grep 20