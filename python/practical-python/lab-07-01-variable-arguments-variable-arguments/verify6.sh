#!/bin/zsh
grep -q "*data" ~/.python_history && grep -q "from" ~/.python_history && echo "True"
