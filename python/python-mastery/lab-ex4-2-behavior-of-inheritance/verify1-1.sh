#!/bin/bash

if grep -q "class A:" ~/.python_shell_history || grep -q "class Base:" ~/.python_shell_history; then
  exit 0
else
  exit 1
fi
