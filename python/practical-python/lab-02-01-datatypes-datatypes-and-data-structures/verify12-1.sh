#!/bin/zsh
(grep -q "d={" ~/.python_history || grep -q "d = {" ~/.python_history) && grep -q "}" ~/.python_history && grep -q "d\[" ~/.python_history && echo "True"
