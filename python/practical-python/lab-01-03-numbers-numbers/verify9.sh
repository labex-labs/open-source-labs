#!/bin/zsh
(python3 ~/project/mortgage.py > debug4 && grep "880074.09999999" debug4) && echo "True"
