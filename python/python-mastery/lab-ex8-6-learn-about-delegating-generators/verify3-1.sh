#!/bin/bash
cd /home/labex/project

# Check if the GenSocket class is defined
if grep -q "class GenSocket" server.py; then
  # Check if accept, recv, and send methods are implemented
  if grep -q "def accept" server.py && grep -q "def recv" server.py && grep -q "def send" server.py; then
    # Check if yield from is used in the tcp_server function
    if grep -q "yield from sock.accept" server.py; then
      echo "Success: Found GenSocket class with proper implementation and usage"
      exit 0
    else
      echo "Error: The tcp_server function doesn't use yield from with GenSocket"
      exit 1
    fi
  else
    echo "Error: GenSocket class is missing required methods"
    exit 1
  fi
else
  echo "Error: Could not find GenSocket class in server.py"
  exit 1
fi
