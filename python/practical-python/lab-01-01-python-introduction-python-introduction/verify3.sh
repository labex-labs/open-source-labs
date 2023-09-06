#!/bin/zsh
(cat ~/.python_history | grep "print") && (cat ~/.python_history | grep "python") && echo "True"

