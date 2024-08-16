#!/bin/bash
grep -q 'echo "price' /home/labex/project/variables.sh \
  && grep -q 'echo "first' /home/labex/project/variables.sh \
  && grep -q 'greeting' /home/labex/project/variables.sh
if [ $? -eq 0 ]; then
  exit 0
else
  exit 1
fi
