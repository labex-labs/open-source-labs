#!/bin/bash
if grep -q "try:" /home/labex/project/cofollow.py && grep -q "except Exception as e:" /home/labex/project/cofollow.py && grep -q "print('ERROR: %r' % e)" /home/labex/project/cofollow.py; then
  echo "Success: The cofollow.py file has been properly modified."
  exit 0
else
  echo "Error: The cofollow.py file has not been modified correctly. Make sure you added the try-except block to handle exceptions."
  exit 1
fi
