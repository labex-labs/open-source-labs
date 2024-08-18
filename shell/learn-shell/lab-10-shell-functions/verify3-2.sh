#!/bin/bash
if grep -q "set_global_result()" ~/project/functions.sh; then
  exit 0
else
  exit 1
fi
