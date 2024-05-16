#!/bin/zsh

# Check if the line "day = days + 1" or "day=days+1" exists in the file ~/project/sears.py
line_exists=$(grep -E "day\s*=\s*days\s*\+\s*1" ~/project/sears.py)

# If the line exists, print "True"
if [ -n "$line_exists" ]; then
  echo "True"
fi
