#!/bin/bash
if grep -q "second_name=\${NAMES\[1\]}" ~/project/arrays.sh; then
  exit 0
else
  exit 1
fi
