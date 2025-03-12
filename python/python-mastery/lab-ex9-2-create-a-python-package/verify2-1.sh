#!/bin/bash

cd /home/labex/project

if [ -d "structly" ]; then
  echo "Package directory exists."
else
  echo "structly directory not found."
  exit 1
fi

if [ -f "structly/__init__.py" ]; then
  echo "__init__.py file exists."
else
  echo "__init__.py file not found in the structly directory."
  exit 1
fi

if [ -f "structly/structure.py" ] && [ -f "structly/validate.py" ] && [ -f "structly/reader.py" ] && [ -f "structly/tableformat.py" ]; then
  echo "All required Python modules moved to the structly package."
  exit 0
else
  echo "Not all required Python modules were moved to the structly package."
  exit 1
fi
