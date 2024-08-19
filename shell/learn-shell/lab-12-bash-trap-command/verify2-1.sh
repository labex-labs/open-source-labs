#!/bin/bash
if grep -q "trap" ~/project/trap_example.sh; then
  exit 0
else
  exit 1
fi
