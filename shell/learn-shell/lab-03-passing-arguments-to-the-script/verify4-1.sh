#!/bin/bash
output=$(./arguments.sh hello world example)
if echo "$output" | grep -q "hello"; then
  exit 0
else
  exit 1
fi
