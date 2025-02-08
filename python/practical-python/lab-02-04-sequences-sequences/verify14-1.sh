#!/bin/zsh
(cat ~/project/pcost.py | grep -q "enumerate(") && python3 ~/project/pcost.py > debug && grep "51.23" debug && echo "True"
