#!/bin/bash
if grep -q "from readport import read_portfolio" ~/.python_history && grep -q "portfolio = read_portfolio" ~/.python_history && grep -q "pprint" ~/.python_history; then
  exit 0
else
  exit 1
fi
