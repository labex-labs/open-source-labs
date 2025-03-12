#!/bin/bash

if grep -q "isinstance.*formatter.*TableFormatter" /home/labex/project/tableformat.py; then
  if grep -q "TypeError.*Expected a TableFormatter" /home/labex/project/tableformat.py; then
    echo "Success! Type checking has been correctly implemented."
    exit 0
  else
    echo "The TypeError message is missing or incorrect."
    exit 1
  fi
else
  echo "The type checking using isinstance() is missing or incorrect."
  exit 1
fi
