#!/bin/bash
output=$(bash /home/labex/project/if.sh)
if [[ $output == *"Harrison"* ]]; then
  exit 0
else
  exit 1
fi
