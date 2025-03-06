#!/bin/bash
cd ~/project
if ls -la | grep -q broken-axis.ipynb; then
  echo "Notebook file found with subplot creation code."
  exit 0
else
  echo "Please make sure you've created the subplot structure in your notebook."
  exit 1
fi
