#!/bin/zsh
(grep -q "while" ~/.python_history) && (grep -q "Name" ~/.python_history || grep -q "name" ~/.python_history || grep -q "NAME" ~/.python_history) && echo "True"
