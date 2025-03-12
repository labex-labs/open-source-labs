#!/bin/bash
HIST_FILE="/home/labex/.python_shell_history"

if grep -q "goog.__dict__" "$HIST_FILE" && grep -q "ibm.__dict__" "$HIST_FILE"; then
  exit 0
else
  exit 1
fi
