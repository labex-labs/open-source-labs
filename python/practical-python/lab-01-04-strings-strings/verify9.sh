#!/bin/zsh
(grep -q "data" ~/.python_history && grep -q "replace" ~/.python_history && grep -q "decode" ~/.python_history && grep -q "encode" ~/.python_history) && echo "True"
