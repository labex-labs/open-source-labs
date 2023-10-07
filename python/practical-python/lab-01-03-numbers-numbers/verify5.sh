#!/bin/zsh
grep -q ">=" ~/.python_history && grep -q "<=" ~/.python_history && grep -q "not" ~/.python_history && echo "True"
