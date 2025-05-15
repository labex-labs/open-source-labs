#!/bin/bash
python3 ~/project/fileparse_3.5.py > debug2 && grep "95}" debug2 && echo "True"
