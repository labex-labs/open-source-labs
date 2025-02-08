#!/bin/zsh
grep -q "with" ~/.python_history && grep -q "\[]" ~/.python_history && grep -q "((" ~/.python_history && echo "True"
