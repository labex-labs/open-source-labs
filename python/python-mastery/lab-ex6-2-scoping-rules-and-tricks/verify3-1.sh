#!/bin/bash
if grep -q "_getframe" ~/.python_history; then
  echo "Success: Stack frame inspection experiment was run"
  exit 0
else
  echo "Error: It seems you didn't run the stack frame inspection experiment"
  exit 1
fi
