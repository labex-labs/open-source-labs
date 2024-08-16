#!/bin/bash
source ~/project/fruit_basket.sh
if [ "$COST_PINEAPPLE" = "50" ]; then
  exit 0
else
  exit 1
fi
