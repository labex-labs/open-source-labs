#!/bin/zsh
grep -q "append" ~/.python_history && grep -q "defaultdict" ~/.python_history && echo "True"
