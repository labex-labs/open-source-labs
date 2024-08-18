#!/bin/bash
if grep -q "Invalid operation" ~/project/functions.sh; then
  exit 0
else
  exit 1
fi
