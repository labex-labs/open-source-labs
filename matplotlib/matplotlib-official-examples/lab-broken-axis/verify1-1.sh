#!/bin/bash
cd ~/project
if ls -la | grep -q broken-axis.ipynb; then
  echo "Notebook file found."
  exit 0
else
  echo "Notebook file not found. Please create broken-axis.ipynb."
  exit 1
fi
