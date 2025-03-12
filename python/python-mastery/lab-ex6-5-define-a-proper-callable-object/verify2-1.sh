#!/bin/bash
if [ -f /home/labex/project/validate.py ]; then
  grep -q "ValidatedFunction" /home/labex/project/validate.py \
    && grep -q "__call__" /home/labex/project/validate.py \
    && echo "Great! You've implemented the ValidatedFunction class."
else
  echo "The validate.py file is missing."
fi
