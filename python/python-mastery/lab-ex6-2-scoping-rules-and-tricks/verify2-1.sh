#!/bin/bash
if grep -q "locals" ~/.python_history; then
  echo "Success: locals() experiment was run"
  exit 0
else
  echo "Error: It seems you didn't run the locals() experiment"
  exit 1
fi
