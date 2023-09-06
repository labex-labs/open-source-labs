#!/bin/zsh
grep -q "while" ~/.python_history && grep -q ":" ~/.python_history && echo "True"
