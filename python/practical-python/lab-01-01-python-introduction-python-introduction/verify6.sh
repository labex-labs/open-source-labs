#!/bin/zsh
grep -q "12 + 20" ~/.python_history || grep -q "(3 + 4
         + 5 + 6)" ~/.python_history || grep -q "for i in range(5):" ~/.python_history && echo "True"