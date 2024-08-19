#!/bin/bash
if grep -q "cleanup_and_exit" ~/project/trap_example.sh; then
  exit 0
else
  exit 1
fi
