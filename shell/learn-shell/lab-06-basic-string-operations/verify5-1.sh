#!/bin/bash
if grep -q 'NEW_STRING=${STRING/o/O}' ~/project/string_operations.sh; then
  exit 0
else
  exit 1
fi
