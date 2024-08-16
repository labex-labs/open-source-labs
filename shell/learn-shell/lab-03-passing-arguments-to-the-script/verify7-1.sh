#!/bin/bash
if grep -q "echo.*Total number of arguments: \$#" /home/labex/project/arguments.sh \
  && grep -q "for arg in \"\$@\"" /home/labex/project/arguments.sh \
  && grep -q "echo.*Argument \$count: \$arg" /home/labex/project/arguments.sh; then
  exit 0
else
  exit 1
fi
