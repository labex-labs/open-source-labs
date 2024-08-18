#!/bin/bash
if grep -q "handle_signal()" ~/project/trap_example.sh; then
  exit 0
else
  exit 1
fi
