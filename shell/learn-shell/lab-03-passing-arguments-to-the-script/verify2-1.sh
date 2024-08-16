#!/bin/bash
if grep -q "echo.*Script name.*\$0" /home/labex/project/arguments.sh \
  && grep -q "echo.*First argument.*\$1" /home/labex/project/arguments.sh \
  && grep -q "echo.*Second argument.*\$2" /home/labex/project/arguments.sh \
  && grep -q "echo.*Third argument.*\$3" /home/labex/project/arguments.sh; then
  exit 0
else
  exit 1
fi
