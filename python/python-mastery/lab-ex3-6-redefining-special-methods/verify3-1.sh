#!/bin/bash
grep -q "__enter__" /home/labex/project/redirect.py && grep -q "__exit__" /home/labex/project/redirect.py && test -f /home/labex/project/out.txt
if [ $? -eq 0 ]; then
  echo "Success! You've correctly implemented the context manager."
  exit 0
else
  echo "The context manager was not correctly implemented or the output file was not created."
  exit 1
fi
