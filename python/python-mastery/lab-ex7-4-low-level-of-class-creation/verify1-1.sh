#!/bin/zsh

cat ~/.python_history | grep -E "=.*\{.*:"
cat ~/.python_history | grep "type"
cat ~/.python_history | grep "object"
