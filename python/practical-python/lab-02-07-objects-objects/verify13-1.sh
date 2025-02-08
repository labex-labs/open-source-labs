#!/bin/zsh
grep -q "dowstocks.csv" ~/.python_history && grep -q "{" ~/.python_history && grep -q "zip" ~/.python_history && echo "True"
