#!/bin/bash
HIST_FILE="/home/labex/.python_shell_history"

if grep -q "class SimpleStock" "$HIST_FILE" && grep -q "goog = SimpleStock" "$HIST_FILE" && grep -q "ibm = SimpleStock" "$HIST_FILE"; then
  exit 0
else
  exit 1
fi
