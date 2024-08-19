#!/bin/bash
if grep -q "z=" ~/project/array-comparison.sh; then
  exit 0
else
  exit 1
fi
