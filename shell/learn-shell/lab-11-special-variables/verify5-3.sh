#!/bin/bash
output=$(~/project/at_vs_star.sh "arg with spaces" another_arg "third arg")
if echo "$output" | grep -q "Argument: arg with spaces"; then
  exit 0
else
  exit 1
fi
