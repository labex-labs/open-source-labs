#!/bin/bash
cd /home/labex/project
if [ -f "methods.py" ] && grep -q "class Spam" methods.py && grep -q "@classmethod" methods.py && grep -q "@staticmethod" methods.py && grep -q "@property" methods.py && grep -q "@logged" methods.py; then
  exit 0
else
  exit 1
fi
