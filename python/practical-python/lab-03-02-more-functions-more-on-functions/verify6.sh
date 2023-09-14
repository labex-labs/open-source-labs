#!/bin/zsh
grep -q "divide" ~/.python_history && grep -q "def" ~/.python_history  && echo "True"
