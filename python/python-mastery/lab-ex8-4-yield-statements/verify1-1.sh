#!/bin/bash
if grep -q "except GeneratorExit:" /home/labex/project/follow.py && grep -q "print('Following Done')" /home/labex/project/follow.py; then
  echo "Success: The follow.py file has been properly modified."
  exit 0
else
  echo "Error: The follow.py file has not been modified correctly. Make sure you added the try-except block with GeneratorExit handling."
  exit 1
fi
