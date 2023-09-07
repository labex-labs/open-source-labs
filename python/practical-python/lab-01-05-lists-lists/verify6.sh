#!/bin/zsh
grep -q "split()" ~/.python_history && grep -q "*" ~/.python_history  && echo "True"