#!/bin/bash
if [ -f ~/project/structly/tableformat/formatter.py ]; then
  echo "File exploration complete"
  exit 0
else
  echo "Please examine the formatter.py file"
  exit 1
fi
