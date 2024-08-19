#!/bin/bash
if grep -q "for i in \"\${c\[@\]}\"" ~/project/array-comparison.sh; then
  exit 0
else
  exit 1
fi
