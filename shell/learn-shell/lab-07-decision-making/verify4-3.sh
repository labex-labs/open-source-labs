#!/bin/bash
output=$(bash /home/labex/project/numeric.sh)
if [[ $output == *"exactly 10"* ]]; then
  exit 0
else
  exit 1
fi
