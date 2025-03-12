#!/bin/bash
grep -q "__get__" /home/labex/project/descrip.py \
  && grep -q "__set__" /home/labex/project/descrip.py \
  && grep -q "__delete__" /home/labex/project/descrip.py
if [ $? -eq 0 ]; then
  exit 0
else
  echo "Descriptor class does not contain required magic methods"
  exit 1
fi
