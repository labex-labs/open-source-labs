#!/bin/zsh
grep -q "del" ~/.python_history && grep -q "s\[" ~/.python_history && echo "True"