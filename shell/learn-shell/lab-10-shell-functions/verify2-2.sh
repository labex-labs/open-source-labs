#!/bin/bash
if grep -q "calculate()" ~/project/functions.sh; then
  exit 0
else
  exit 1
fi
