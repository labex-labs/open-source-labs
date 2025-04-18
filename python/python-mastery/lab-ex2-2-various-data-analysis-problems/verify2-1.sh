#!/bin/bash
if grep -q "portfolio" ~/.python_history && grep -q "sum" ~/.python_history && grep -q "name" ~/.python_history; then
  exit 0
else
  exit 1
fi
