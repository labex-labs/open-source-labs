#!/bin/bash
grep -q 'price' /home/labex/project/variables.sh \
  && grep -q 'first' /home/labex/project/variables.sh \
  && grep -q 'greeting' /home/labex/project/variables.sh
if [ $? -eq 0 ]; then
  exit 0
else
  exit 1
fi
