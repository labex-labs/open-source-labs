#!/bin/bash
output=$(./arguments.sh hello world example)
if echo "$output" | grep -q "Script name.*arguments.sh" \
  && echo "$output" | grep -q "First argument.*hello" \
  && echo "$output" | grep -q "Second argument.*world" \
  && echo "$output" | grep -q "Third argument.*example"; then
  exit 0
else
  exit 1
fi
