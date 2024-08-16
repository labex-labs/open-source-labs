#!/bin/bash
if grep -q "echo \"Total Cost is \$TOTAL cents\"" ~/project/fruit_basket.sh; then
  exit 0
else
  exit 1
fi
