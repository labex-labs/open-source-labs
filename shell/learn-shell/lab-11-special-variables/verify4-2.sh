#!/bin/bash
if grep -q "function print_args" ~/project/function_vars.sh; then
  exit 0
else
  exit 1
fi
