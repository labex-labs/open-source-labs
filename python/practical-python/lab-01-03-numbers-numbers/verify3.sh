#!/bin/zsh
grep -q "0b" ~/.python_history && grep -q "0o" ~/.python_history && grep -q "-" ~/.python_history && grep -q "0x" ~/.python_history && echo "True"
