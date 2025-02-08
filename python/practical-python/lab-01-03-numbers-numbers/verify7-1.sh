#!/bin/zsh
(python3 ~/project/mortgage.py > debug2 && grep "966" debug2) && echo "True"
