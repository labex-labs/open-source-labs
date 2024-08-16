#!/bin/bash
if grep -q "NumberOfNames=\${#NAMES\[@\]}" ~/project/arrays.sh; then
  exit 0
else
  exit 1
fi
