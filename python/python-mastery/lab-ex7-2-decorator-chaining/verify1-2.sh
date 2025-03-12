#!/bin/bash
cd /home/labex/project
if grep -q "from functools import wraps" validate.py && grep -q "@wraps" validate.py; then
  exit 0
else
  exit 1
fi
