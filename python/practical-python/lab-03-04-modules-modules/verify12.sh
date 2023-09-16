#!/bin/zsh
grep -q "from fileparse import parse_csv" ~/.python_history && grep -q "import fileparse" ~/.python_history && echo "True"
