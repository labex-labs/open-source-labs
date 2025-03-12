#!/bin/bash
cd /home/labex/project
if grep -q "def logformat" logcall.py && grep -q "format" logcall.py && grep -q "func=" logcall.py; then
  exit 0
else
  exit 1
fi
