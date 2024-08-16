#!/bin/bash
grep -q 'CURRENT_DATE=$(date +"%Y-%m-%d")' /home/labex/project/variables.sh \
  && grep -q 'FILES_IN_DIR=$(ls)' /home/labex/project/variables.sh \
  && grep -q 'UPTIME=$(uptime -p)' /home/labex/project/variables.sh
if [ $? -eq 0 ]; then
  exit 0
else
  exit 1
fi
