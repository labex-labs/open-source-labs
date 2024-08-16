#!/bin/bash
if grep -q "\[ \$# -eq 0 \]" /home/labex/project/arguments.sh \
  && grep -q "\[ \$# -eq 1 \]" /home/labex/project/arguments.sh \
  && grep -q "\[ \$# -eq 2 \]" /home/labex/project/arguments.sh \
  && grep -q "Total number of arguments: \$#" /home/labex/project/arguments.sh; then
  exit 0
else
  exit 1
fi
