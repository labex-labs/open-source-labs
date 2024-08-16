#!/bin/bash
if grep -q "NUMBERS+=(1)" ~/project/arrays.sh \
  && grep -q 'STRINGS+=("hello")' ~/project/arrays.sh \
  && grep -q 'NAMES+=("John")' ~/project/arrays.sh; then
  exit 0
else
  exit 1
fi
