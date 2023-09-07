#!/bin/zsh
(grep -q "help" ~/.python_history) && (grep -q "dir" ~/.python_history) && (grep -q "<tab key>" ~/.python_history) && echo "True"