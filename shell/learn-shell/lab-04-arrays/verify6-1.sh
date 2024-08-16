#!/bin/bash
if grep -q 'echo' ~/project/arrays.sh; then
  exit 0
else
  exit 1
fi
