#!/bin/bash
if [ -d "/home/labex/.local/lib/python3.10/site-packages/matplotlib" ]; then
  echo "Matplotlib is installed correctly."
  exit 0
else
  echo "Matplotlib is not installed. Please make sure you run the import statement."
  exit 1
fi
