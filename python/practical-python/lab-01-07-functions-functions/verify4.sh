#!/bin/zsh
grep -q "except" ~/.python_history && grep -q "for" ~/.python_history && grep -q "in" ~/.python_history && grep -q "try" ~/.python_history && echo "True"
