#!/bin/zsh
grep -q "while" ~/.python_history && grep -q ":" ~/.python_history && grep -q "print" ~/.python_history && echo "True"
