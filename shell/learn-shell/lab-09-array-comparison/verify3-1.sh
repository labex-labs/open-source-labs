#!/bin/zsh
if grep -q "for x in \"\${a\[@\]}\"" ~/project/array-comparison.sh; then
  exit 0
else
  exit 1
fi
