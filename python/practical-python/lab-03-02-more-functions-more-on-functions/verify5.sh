#!/bin/zsh
grep -q "return" ~/.python_history && grep -q "def" ~/.python_history && echo "True"
