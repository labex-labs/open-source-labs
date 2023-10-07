#!/bin/zsh
grep -q "import csv" ~/.python_history && grep -q "*" ~/.python_history && echo "True"