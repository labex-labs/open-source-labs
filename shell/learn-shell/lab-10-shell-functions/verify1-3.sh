#!/bin/bash
if grep -q "greet()" ~/project/functions.sh; then
  exit 0
else
  exit 1
fi
