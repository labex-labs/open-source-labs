#!/bin/bash

cd /home/labex/project
if grep -q "property" stock.py; then
  exit 0
else
  exit 1
fi
