#!/bin/bash
cd /home/labex/project
if grep -q "from functools import wraps" logcall.py && grep -q "@wraps" logcall.py; then
  exit 0
else
  exit 1
fi
