#!/bin/bash
if grep -q 'SUBSTRING=${STRING:$START:$LENGTH}' ~/project/string_operations.sh; then
  exit 0
else
  exit 1
fi
