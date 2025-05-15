#!/bin/bash
python3 ~/project/fileparse_3.6.py > debug3 && grep "AXP" debug3 && echo "True"
