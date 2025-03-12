#!/bin/bash
if grep -q "class ColumnFormatMixin" "/home/labex/project/tableformat.py" && grep -q "class UpperHeadersMixin" "/home/labex/project/tableformat.py"; then
  exit 0
else
  echo "One or both mixin classes are missing in tableformat.py"
  exit 1
fi
