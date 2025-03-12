#!/bin/bash
if [[ -f ~/project/readport.py && -f ~/project/readrides.py ]]; then
  exit 0
else
  exit 1
fi
