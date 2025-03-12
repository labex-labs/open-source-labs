#!/bin/bash
if [ -f /home/labex/project/validate.py ]; then
  grep -q "Validator" /home/labex/project/validate.py \
    && echo "Great! You've examined the validator classes."
else
  echo "The validate.py file is missing."
fi
