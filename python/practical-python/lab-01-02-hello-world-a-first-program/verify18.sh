#!/bin/zsh
(python3 ~/project/bounce.py > run && grep "60" run) && echo "True"
