#!/bin/bash
cd ~/project
if [ -f titles-demo.ipynb ]; then
  echo "Excellent work on customizing title vertical positions!"
  exit 0
else
  echo "Could not find the titles-demo.ipynb notebook. Please make sure you've created it."
  exit 1
fi
