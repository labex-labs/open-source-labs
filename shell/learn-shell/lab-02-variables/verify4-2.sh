#!/bin/bash
grep -q 'SUM' /home/labex/project/arithmetic.sh \
  && grep -q 'DIFF' /home/labex/project/arithmetic.sh \
  && grep -q 'PRODUCT' /home/labex/project/arithmetic.sh \
  && grep -q 'QUOTIENT' /home/labex/project/arithmetic.sh \
  && grep -q 'REMAINDER' /home/labex/project/arithmetic.sh \
  && grep -q 'X' /home/labex/project/arithmetic.sh \
  && grep -q 'Y' /home/labex/project/arithmetic.sh
if [ $? -eq 0 ]; then
  exit 0
else
  exit 1
fi
