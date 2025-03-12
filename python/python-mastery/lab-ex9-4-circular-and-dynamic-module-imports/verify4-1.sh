#!/bin/bash
if grep -q "__import__" ~/project/structly/tableformat/formatter.py && ! grep -q "from .formats.text import" ~/project/structly/tableformat/formatter.py; then
  echo "Dynamic imports have been implemented correctly"
  exit 0
else
  echo "Please implement dynamic imports and remove the static imports"
  exit 1
fi
