#!/bin/zsh

cat /home/labex/project/validate.py | grep -E "@.*[a-z]*" | grep -v "@classmethod"
