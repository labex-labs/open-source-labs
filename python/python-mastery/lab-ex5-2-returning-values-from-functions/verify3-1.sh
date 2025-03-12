#!/bin/bash
if grep -q "ThreadPoolExecutor" /home/labex/project/futures_demo.py && grep -q "future.result" /home/labex/project/futures_demo.py; then
  exit 0
else
  exit 1
fi
