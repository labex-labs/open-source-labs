#!/bin/zsh
(cat ~/.python_history | grep "sum") && (cat ~/.python_history | grep "min") && (cat ~/.python_history | grep "max") && echo "True"
