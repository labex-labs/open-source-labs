#!/bin/zsh
((grep -q "=Player" ~/.python_history)||(grep -q "= Player" ~/.python_history)) && echo "True"


