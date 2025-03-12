#!/bin/bash
# Check if the __eq__ method is defined in structure.py
grep -q "__eq__" /home/labex/project/structure.py && echo "Success" || echo "Failure: __eq__ method not found in structure.py"
