#!/bin/bash
if grep -q "case \$operation in" ~/project/functions.sh; then
  exit 0
else
  exit 1
fi
