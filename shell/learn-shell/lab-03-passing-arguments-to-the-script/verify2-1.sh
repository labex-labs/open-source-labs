#!/bin/bash
if grep -q "\$0" /home/labex/project/arguments.sh; then
  exit 0
else
  exit 1
fi
