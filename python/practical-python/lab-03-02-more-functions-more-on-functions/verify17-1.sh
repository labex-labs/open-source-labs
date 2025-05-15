#!/bin/bash
python3 ~/project/fileparse_3.7.py > debug4 && grep "'shares': 95" debug4 && echo "True"
