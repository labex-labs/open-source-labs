#!/bin/bash
if grep -q "for name in" /home/labex/project/bash_loops/for_loop.sh; then
  exit 0
else
  exit 1
fi
