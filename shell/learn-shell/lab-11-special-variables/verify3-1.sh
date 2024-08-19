#!/bin/bash
if [[ -f ~/project/exit_status.sh ]]; then
  exit 0
else
  exit 1
fi
