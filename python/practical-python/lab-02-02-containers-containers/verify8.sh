#!/bin/zsh
grep -q "set" ~/.python_history && grep -q "add" ~/.python_history && echo "True"
