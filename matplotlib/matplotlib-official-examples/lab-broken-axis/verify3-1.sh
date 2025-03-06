#!/bin/bash
cd ~/project
if ls -la | grep -q broken-axis.ipynb; then
  echo "Notebook file found with complete plot code."
  exit 0
else
  echo "Please make sure you've added the diagonal break lines to your plot."
  exit 1
fi
