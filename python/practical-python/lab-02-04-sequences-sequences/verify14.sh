#!/bin/zsh
(python3 ~/project/pcost.py > debug && grep "51.23" debug) && echo "True"