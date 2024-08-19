#!/bin/bash
if grep -q "Script Name: \$0" ~/project/special_vars.sh; then
  exit 0
else
  exit 1
fi
