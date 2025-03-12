#!/bin/bash
if grep -q "s for s in portfolio if s" ~/.python_history && grep -q "sum..*s..*shares..*s..*price" ~/.python_history && grep -q "s..*name..*for s in portfolio" ~/.python_history; then
  exit 0
else
  exit 1
fi
