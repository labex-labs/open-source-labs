#!/bin/zsh
grep -q "[
  (" ~/.python_history || grep -q "[(" ~/.python_history && echo "True"