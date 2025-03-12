#!/bin/bash
if [[ -f /home/labex/project/tableformat.py ]] && grep -q "print_table" /home/labex/project/tableformat.py; then
  exit 0
else
  exit 1
fi
