#!/bin/bash
if grep -q "__self__" /home/labex/.python_history && grep -q "__func__" /home/labex/.python_history; then
  exit 0
else
  exit 1
fi
