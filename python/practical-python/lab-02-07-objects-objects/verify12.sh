#!/bin/zsh
grep -q "dict" ~/.python_history && grep -q "{" ~/.python_history && grep -q "zip" ~/.python_history && echo "True"
