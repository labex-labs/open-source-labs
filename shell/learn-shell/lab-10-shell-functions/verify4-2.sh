#!/bin/bash
if grep -q "local LOCAL_VAR" ~/project/functions.sh; then
  exit 0
else
  exit 1
fi
