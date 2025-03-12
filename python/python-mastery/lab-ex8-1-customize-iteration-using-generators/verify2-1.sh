#!/bin/bash
# Check if the __iter__ method is defined in structure.py
grep -q "__iter__" /home/labex/project/structure.py && echo "Success" || echo "Failure: __iter__ method not found in structure.py"
