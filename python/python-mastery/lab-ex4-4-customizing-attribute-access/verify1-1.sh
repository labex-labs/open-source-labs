#!/bin/bash
grep -q "__setattr__" /home/labex/project/restricted_stock.py && echo "Success" || echo "Fail: Cannot find __setattr__ method in restricted_stock.py"
