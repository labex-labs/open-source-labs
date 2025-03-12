#!/bin/bash
grep -q "__getattr__" /home/labex/project/delegator.py && echo "Success" || echo "Fail: Cannot find __getattr__ method in delegator.py"
