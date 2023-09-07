#!/bin/zsh
(python3 ~/project/pcost.py missing.csv > debug2 && ! grep "rror" debug2) && echo "True"
