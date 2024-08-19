#!/bin/bash
if grep -q "for arg in \"\$@\"" ~/project/at_vs_star.sh; then
  exit 0
else
  exit 1
fi
