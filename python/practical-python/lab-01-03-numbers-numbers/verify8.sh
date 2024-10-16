#!/bin/zsh
(python3 ~/project/mortgage.py > debug3 && grep "929965" debug3) && echo "True"
