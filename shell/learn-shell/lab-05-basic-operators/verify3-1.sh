#!/bin/bash
if grep -q "TOTAL=\$((COST_PINEAPPLE + (COST_BANANA \* 2) + (COST_WATERMELON \* 3) + COST_BASKET))" ~/project/fruit_basket.sh; then
  exit 0
else
  exit 1
fi
