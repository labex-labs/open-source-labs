#!/bin/bash
if grep -q "open" ~/project/pcost.py && grep -q "for line in file" ~/project/pcost.py; then
  exit 0
else
  exit 1
fi
