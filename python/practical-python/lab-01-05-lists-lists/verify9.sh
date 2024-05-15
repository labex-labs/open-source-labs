#!/bin/zsh
grep -q "in symlist" ~/.python_history && grep -q "not in symlist" ~/.python_history && echo "True"
