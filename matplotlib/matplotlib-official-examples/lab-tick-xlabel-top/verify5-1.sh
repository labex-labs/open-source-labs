#!/bin/bash
if [ -f "/home/labex/project/plot_with_top_xlabels.png" ]; then
  echo "Plot files have been saved successfully."
  exit 0
else
  echo "Plot files have not been saved. Please run the code that saves the plot."
  exit 1
fi
