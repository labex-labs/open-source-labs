#!/bin/zsh
cat ~/.python_history | grep -q ":" && cat ~/.python_history | grep -q "\[" && echo "True"
