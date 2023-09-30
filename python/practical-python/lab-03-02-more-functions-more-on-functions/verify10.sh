#!/bin/zsh
grep -q "global n" ~/.python_history && grep -q "def" ~/.python_history  && echo "True"
