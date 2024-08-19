#!/bin/bash
if grep -q "j=" ~/project/array-comparison.sh; then
  exit 0
else
  exit 1
fi
