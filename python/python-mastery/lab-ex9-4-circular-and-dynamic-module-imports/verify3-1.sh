#!/bin/bash
if grep -q "_formats" ~/project/structly/tableformat/formatter.py && grep -q "__init_subclass__" ~/project/structly/tableformat/formatter.py; then
  echo "TableFormatter class has been updated correctly"
  exit 0
else
  echo "Please implement the registration mechanism in TableFormatter class"
  exit 1
fi
