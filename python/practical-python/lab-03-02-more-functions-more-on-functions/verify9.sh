#!/bin/zsh
grep -q "print" ~/.python_history && grep -q "def" ~/.python_history && echo "True"
