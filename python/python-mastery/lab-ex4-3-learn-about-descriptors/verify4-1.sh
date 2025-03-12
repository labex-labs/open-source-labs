#!/bin/bash
grep -q "__set_name__" /home/labex/project/validate.py
if [ $? -eq 0 ]; then
  exit 0
else
  echo "The __set_name__ method is missing from the Validator class"
  exit 1
fi
