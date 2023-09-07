#!/bin/zsh
grep -q "\n" ~/.python_history && grep -q "\t" ~/.python_history && echo "True"