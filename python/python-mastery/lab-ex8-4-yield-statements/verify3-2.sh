#!/bin/bash
if [ -f /home/labex/project/pipeline.py ] && grep -q "@consumer" /home/labex/project/pipeline.py && grep -q "follow_and_process" /home/labex/project/pipeline.py; then
  echo "Success: The pipeline.py file has been created correctly."
  exit 0
else
  echo "Error: The pipeline.py file is missing or does not include the required pipeline functionality."
  exit 1
fi
