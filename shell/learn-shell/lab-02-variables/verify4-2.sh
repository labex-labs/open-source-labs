#!/bin/bash
grep -q 'SUM=$((X + Y))' /home/labex/project/arithmetic.sh \
  && grep -q 'DIFF=$((X - Y))' /home/labex/project/arithmetic.sh \
  && grep -q 'PRODUCT=$((X * Y))' /home/labex/project/arithmetic.sh \
  && grep -q 'QUOTIENT=$((X / Y))' /home/labex/project/arithmetic.sh \
  && grep -q 'REMAINDER=$((X % Y))' /home/labex/project/arithmetic.sh \
  && grep -q 'X=$((X + 1))' /home/labex/project/arithmetic.sh \
  && grep -q 'Y=$((Y - 1))' /home/labex/project/arithmetic.sh
if [ $? -eq 0 ]; then
  exit 0
else
  exit 1
fi
