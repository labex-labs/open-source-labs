#!/bin/zsh
grep -q "append" ~/.python_history && grep -q "def" ~/.python_history  && echo "True"
