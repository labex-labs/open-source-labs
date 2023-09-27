#!/bin/zsh
grep -q ":" ~/.python_history && grep -q "holidays\[" ~/.python_history && echo "True"