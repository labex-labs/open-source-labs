#!/bin/bash

# Check if TextTableFormatter class exists with required methods
if grep -q "class TextTableFormatter" /home/labex/project/tableformat.py \
  && grep -q "def headings.*headers" /home/labex/project/tableformat.py \
  && grep -q "def row.*rowdata" /home/labex/project/tableformat.py; then
  exit 0
else
  echo "TextTableFormatter class not found or missing required methods."
  exit 1
fi
