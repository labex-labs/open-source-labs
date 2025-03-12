#!/bin/bash
if [ -f /home/labex/project/validate.py ]; then
  grep -q "__annotations__" /home/labex/project/validate.py \
    && grep -q "signature" /home/labex/project/validate.py \
    && echo "Great! You've implemented the validation logic."
else
  echo "The validate.py file is missing."
fi
