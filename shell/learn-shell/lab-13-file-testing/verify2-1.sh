#!/bin/bash
if [[ -f test_file.txt ]] && grep -q "test file" test_file.txt; then
  exit 0
else
  exit 1
fi
