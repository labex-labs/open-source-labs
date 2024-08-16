#!/bin/bash
output=$(~/project/fruit_basket.sh)
if [[ "$output" == *"Total Cost is 128 cents"* ]]; then
  exit 0
else
  exit 1
fi
