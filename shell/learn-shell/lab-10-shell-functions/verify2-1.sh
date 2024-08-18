#!/bin/bash
if grep -q 'echo "Hello, $1!"' ~/project/functions.sh; then
  exit 0
else
  exit 1
fi
