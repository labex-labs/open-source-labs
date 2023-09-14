#!/bin/zsh
grep -q "global" ~/.python_history && grep -q "def" ~/.python_history  && echo "True"
