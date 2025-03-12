#!/bin/bash
HIST_FILE="/home/labex/.python_shell_history"

if grep -q "goog.date =" "$HIST_FILE" && grep -q "goog.__dict__\['time'\] =" "$HIST_FILE"; then
  exit 0
else
  exit 1
fi
