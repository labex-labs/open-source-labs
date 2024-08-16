#!/bin/bash
grep -q "PRICE_PER_APPLE=5" /home/labex/project/variables.sh \
  && grep -q "MyFirstLetters=ABC" /home/labex/project/variables.sh \
  && grep -q "greeting='Hello        world!'" /home/labex/project/variables.sh
if [ $? -eq 0 ]; then
  exit 0
else
  exit 1
fi
