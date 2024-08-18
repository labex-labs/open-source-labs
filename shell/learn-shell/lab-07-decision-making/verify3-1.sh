#!/bin/bash
if grep -q "elif" "/home/labex/project/if.sh"; then
  exit 0
else
  exit 1
fi
