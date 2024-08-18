#!/bin/bash
if grep -q "demonstrate_scope()" ~/project/functions.sh; then
  exit 0
else
  exit 1
fi
