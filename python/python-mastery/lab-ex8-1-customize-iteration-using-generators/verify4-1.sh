#!/bin/bash
# Check if follow.py exists and contains the follow generator function
if [ -f /home/labex/project/follow.py ]; then
  grep -q "def follow" /home/labex/project/follow.py && echo "Success" || echo "Failure: follow generator function not found in follow.py"
else
  echo "Failure: follow.py file not found"
fi
