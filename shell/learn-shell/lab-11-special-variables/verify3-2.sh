#!/bin/bash
if grep -q "Exit status: \$?" ~/project/exit_status.sh; then
  exit 0
else
  exit 1
fi
