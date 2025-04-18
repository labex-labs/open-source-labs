#!/bin/bash
if grep -q "collections" ~/.python_history && grep -q "defaultdict" ~/.python_history && grep -q "byname" ~/.python_history; then
  exit 0
else
  exit 1
fi
