#!/bin/bash
if grep -q "until \[ \$count -gt 5 ]" /home/labex/project/bash_loops/until_loop.sh; then
  exit 0
else
  exit 1
fi
