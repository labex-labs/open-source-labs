#!/bin/zsh
grep -q "print" ~/.python_history && grep -q "input" ~/.python_history && echo "True"
