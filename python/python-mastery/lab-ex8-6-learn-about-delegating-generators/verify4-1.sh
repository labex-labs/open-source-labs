#!/bin/bash
cd /home/labex/project

# Check if coroutine is imported from types
if grep -q "from types import coroutine" server.py; then
  # Check if async def is used
  if grep -q "async def" server.py; then
    # Check if await is used
    if grep -q "await" server.py; then
      echo "Success: Found async/await implementation"
      exit 0
    else
      echo "Error: The async functions don't use await"
      exit 1
    fi
  else
    echo "Error: Could not find async def in server.py"
    exit 1
  fi
else
  echo "Error: Could not find 'from types import coroutine' import in server.py"
  exit 1
fi
