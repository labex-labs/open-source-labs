#!/bin/bash
if [[ -f ~/project/special_vars.sh ]]; then
  exit 0
else
  exit 1
fi
