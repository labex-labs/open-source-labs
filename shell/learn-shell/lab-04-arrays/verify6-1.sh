#!/bin/bash
if grep -q 'echo "NUMBERS array: ${NUMBERS[@]}"' ~/project/arrays.sh \
  && grep -q 'echo "The second name on the NAMES list is: $second_name"' ~/project/arrays.sh; then
  exit 0
else
  exit 1
fi
