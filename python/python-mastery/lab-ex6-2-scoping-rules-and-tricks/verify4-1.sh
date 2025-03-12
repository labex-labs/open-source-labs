#!/bin/bash
if grep -q "_init" /home/labex/project/structure.py && grep -q "sys._getframe" /home/labex/project/structure.py; then
  echo "Success: Structure class has been updated with frame inspection"
  exit 0
else
  echo "Error: structure.py does not contain the required changes"
  exit 1
fi
