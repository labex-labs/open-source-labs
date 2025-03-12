#!/bin/bash
if grep -q "getattr" /home/labex/.python_history && grep -q "setattr" /home/labex/.python_history && grep -q "hasattr" /home/labex/.python_history; then
  exit 0
else
  exit 1
fi
