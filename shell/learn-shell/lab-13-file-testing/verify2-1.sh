#!/bin/bash
cd ~/project
if [[ -f file_exists.sh ]] && grep -q "filename=" file_exists.sh; then
  exit 0
else
  exit 1
fi
