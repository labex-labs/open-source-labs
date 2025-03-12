#!/bin/bash

HISTORY_FILE="/home/labex/.python_shell_history.json"

if [ ! -f "$HISTORY_FILE" ]; then
  echo "Python shell history file not found."
  exit 1
fi

if grep -q "__init__.*self.*name.*shares.*price" "$HISTORY_FILE" \
  && grep -q "cost.*self.*return.*shares.*price" "$HISTORY_FILE" \
  && grep -q "sell.*self.*nshares" "$HISTORY_FILE" \
  && grep -q "methods.*=.*{.*__init__.*:.*__init__" "$HISTORY_FILE" \
  && grep -q "Stock.*=.*type.*'Stock'.*object" "$HISTORY_FILE" \
  && grep -q "s.*=.*Stock.*'GOOG'.*100" "$HISTORY_FILE"; then
  exit 0
else
  echo "Could not verify all required Python commands were executed."
  exit 1
fi
