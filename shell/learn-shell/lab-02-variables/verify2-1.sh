#!/bin/bash
grep -q 'echo "The price of an Apple today is: \$HK $PRICE_PER_APPLE"' /home/labex/project/variables.sh \
  && grep -q 'echo "The first 10 letters in the alphabet are: ${MyFirstLetters}DEFGHIJ"' /home/labex/project/variables.sh \
  && grep -q 'echo "$greeting"' /home/labex/project/variables.sh
if [ $? -eq 0 ]; then
  exit 0
else
  exit 1
fi
