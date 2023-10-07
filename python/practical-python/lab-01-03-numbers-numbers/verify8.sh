#!/bin/zsh
(python3 ~/project/mortgage.py > debug3 && grep "929965.61999999" debug3) && echo "True"
