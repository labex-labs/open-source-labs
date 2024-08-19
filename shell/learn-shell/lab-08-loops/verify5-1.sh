#!/bin/bash
if grep -q "break" /home/labex/project/bash_loops/break_continue.sh && grep -q "continue" /home/labex/project/bash_loops/break_continue.sh; then
  exit 0
else
  exit 1
fi
