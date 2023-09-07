#!/bin/zsh
grep -q ".get" ~/.python_history && grep -q "if" ~/.python_history && grep -q "in" ~/.python_history && echo "True"