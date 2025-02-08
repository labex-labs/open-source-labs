#!/bin/zsh
grep -q "def" ~/.python_history && grep -q "import" ~/.python_history && echo "True"
