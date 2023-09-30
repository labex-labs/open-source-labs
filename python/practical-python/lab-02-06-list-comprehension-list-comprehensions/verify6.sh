#!/bin/zsh
grep -q "*" ~/.python_history && grep -q "squares" ~/.python_history && grep -q "for" ~/.python_history && grep -q "\]" ~/.python_history && grep -q "\[" ~/.python_history && echo "True"