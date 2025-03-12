#!/bin/bash
HIST_FILE="/home/labex/.python_shell_history"

if grep -q "__class__" "$HIST_FILE" && grep -q "SimpleStock\.__dict__\['cost'\]" "$HIST_FILE" && grep -q "SimpleStock\.exchange =" "$HIST_FILE"; then
  exit 0
else
  exit 1
fi
