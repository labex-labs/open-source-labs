#!/bin/bash
python_history=$(cat ~/.python_history 2> /dev/null)
if echo "$python_history" | grep -q "from follow import follow" \
  && echo "$python_history" | grep -q "import csv" \
  && echo "$python_history" | grep -q "lines = follow" \
  && echo "$python_history" | grep -q "rows = csv.reader"; then
  exit 0
else
  exit 1
fi
