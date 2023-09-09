#!/bin/zsh
grep -q "while num_bills * bill_thickness < sears_height:
print" ~/.python_history && grep -q ":" ~/.python_history && grep -q "print" ~/.python_history && echo "True"
