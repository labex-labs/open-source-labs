#!/bin/zsh
(python3 ~/project/mortgage.py > debug4 && grep "853655" debug4) && echo "True"
