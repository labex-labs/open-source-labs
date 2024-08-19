#!/bin/bash
output=$(~/project/exit_status.sh)
if echo "$output" | grep -q "Exit status: 0"; then
  exit 0
else
  exit 1
fi
