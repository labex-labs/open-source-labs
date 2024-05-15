#!/bin/zsh
grep -q "\[" ~/.python_history && grep -q "for" ~/.python_history && echo "True"
