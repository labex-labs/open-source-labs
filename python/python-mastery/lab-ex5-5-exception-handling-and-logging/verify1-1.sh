#!/bin/bash

# Check if the user has examined the project files
if [ -f /home/labex/project/reader.py ]; then
  exit 0
else
  echo "The reader.py file should be in the /home/labex/project directory"
  exit 1
fi
