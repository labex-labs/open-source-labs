#!/bin/bash
if grep -q "NUMBERS=()" ~/project/arrays.sh \
  && grep -q "STRINGS=()" ~/project/arrays.sh \
  && grep -q "NAMES=()" ~/project/arrays.sh; then
  exit 0
else
  exit 1
fi
