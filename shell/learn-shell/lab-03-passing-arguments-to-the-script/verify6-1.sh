#!/bin/bash
no_args=$(./arguments.sh)
one_arg=$(./arguments.sh one)
two_args=$(./arguments.sh one two)
many_args=$(./arguments.sh one two three four)

if echo "$no_args" | grep -q "No arguments provided" \
  && echo "$one_arg" | grep -q "One argument provided: one" \
  && echo "$two_args" | grep -q "Two arguments provided: one and two" \
  && echo "$many_args" | grep -q "More than two arguments provided" \
  && echo "$many_args" | grep -q "Total number of arguments: 4"; then
  exit 0
else
  exit 1
fi
