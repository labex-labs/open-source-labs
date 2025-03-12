#!/bin/bash
if grep -q "split" ~/project/pcost.py && grep -q "shares" ~/project/pcost.py && grep -q "price" ~/project/pcost.py; then
  exit 0
else
  exit 1
fi
