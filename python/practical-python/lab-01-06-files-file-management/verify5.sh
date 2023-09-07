#!/bin/zsh
(python3 ~/project/pcost.py > debug && grep "44671" debug) && echo "True"
