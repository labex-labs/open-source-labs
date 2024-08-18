#!/bin/bash
if grep -q "trap handle_signal 2 15" ~/project/trap_example.sh; then
  exit 0
else
  exit 1
fi
