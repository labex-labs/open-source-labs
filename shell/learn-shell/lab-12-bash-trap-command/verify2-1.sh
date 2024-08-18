#!/bin/bash
if grep -q "trap \"echo Signal received!\" SIGINT SIGTERM" ~/project/trap_example.sh; then
  exit 0
else
  exit 1
fi
