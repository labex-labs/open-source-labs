#!/bin/bash
if grep -q "read_portfolio" ~/.python_history && grep -q "portfolio" ~/.python_history && grep -q "print" ~/.python_history; then
  exit 0
else
  exit 1
fi
