#!/bin/bash
if grep -q "ENGLISH_CALC()" ~/project/functions.sh; then
  exit 0
else
  exit 1
fi
