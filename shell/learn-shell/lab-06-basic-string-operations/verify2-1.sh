#!/bin/bash
if grep -q 'LENGTH=${#STRING}' ~/project/string_operations.sh; then
  exit 0
else
  exit 1
fi
