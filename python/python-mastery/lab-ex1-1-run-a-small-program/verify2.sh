#!/bin/zsh
python3 art.py 10 20 | awk '{print length}' | grep 20