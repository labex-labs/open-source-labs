#!/bin/bash
if [ -f /home/labex/project/robust_follow.py ] && grep -q "TimeoutError" /home/labex/project/robust_follow.py && grep -q "GeneratorExit" /home/labex/project/robust_follow.py; then
  echo "Success: The robust_follow.py file has been created correctly."
  exit 0
else
  echo "Error: The robust_follow.py file is missing or does not include the required exception handling code."
  exit 1
fi
