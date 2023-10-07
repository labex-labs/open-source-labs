#!/bin/zsh
grep -q "%d" ~/.python_history && grep -q "%b" ~/.python_history && grep -q "%" ~/.python_history && echo "True"