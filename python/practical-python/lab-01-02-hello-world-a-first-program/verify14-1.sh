#!/bin/zsh
grep -q "if" ~/.python_history && grep -q "else:" ~/.python_history && grep -q "elif" ~/.python_history && echo "True"
