#!/bin/bash
if grep -q 'POSITION=$(expr index "$STRING" "$CHAR")' ~/project/string_operations.sh; then
  exit 0
else
  exit 1
fi
