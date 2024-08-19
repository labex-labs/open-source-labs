#!/bin/bash
if grep -q "while \[ \$count -gt 0 ]" /home/labex/project/bash_loops/while_loop.sh; then
  exit 0
else
  exit 1
fi
