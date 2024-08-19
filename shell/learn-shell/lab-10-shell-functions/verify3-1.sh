#!/bin/bash
if grep -q "get_square()" ~/project/functions.sh; then
  exit 0
else
  exit 1
fi
