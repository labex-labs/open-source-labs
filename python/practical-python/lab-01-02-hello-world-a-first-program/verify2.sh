#!/bin/zsh
grep -q "_" ~/.python_history || grep -q "print" ~/.python_history || grep -q "37 * 42" ~/.python_history || grep -q "for i in range(5):" ~/.python_history && echo "True"
