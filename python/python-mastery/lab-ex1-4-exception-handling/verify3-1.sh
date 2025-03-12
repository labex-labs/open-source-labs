#!/bin/bash
if grep -q "portfolio_cost" /home/labex/.python_history; then
  exit 0
else
  echo "No evidence of using portfolio_cost function in interactive mode"
  exit 1
fi
