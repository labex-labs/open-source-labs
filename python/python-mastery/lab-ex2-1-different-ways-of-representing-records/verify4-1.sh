#!/bin/bash
ls /home/labex/project/compare_structures.py > /dev/null 2>&1 && grep -q "namedtuple" /home/labex/project/compare_structures.py && echo "Success"
