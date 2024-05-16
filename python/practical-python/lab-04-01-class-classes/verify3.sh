#!/bin/zsh

# Check if the lines "=Player" or "= Player" exist in the file ~/.python_history
player_line=$(grep -E "^\s*=?\s*Player" ~/.python_history)

# If either line exists, print "True"
if [ -n "$player_line" ]; then
  echo "True"
fi
