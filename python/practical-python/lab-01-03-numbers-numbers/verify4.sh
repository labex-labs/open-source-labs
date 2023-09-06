#!/bin/zsh
grep -q "or" ~/.python_history && grep -q "==" ~/.python_history && grep -q "math" ~/.python_history && grep -q "#" ~/.python_history && echo "True"
