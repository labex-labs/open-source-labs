#!/bin/bash
grep -q "Stock('IBM'" /home/labex/.python_history \
  || grep -q "Stock(\"IBM\"" /home/labex/.python_history || exit 1
