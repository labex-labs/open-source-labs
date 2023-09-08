#!/bin/zsh
(cat ~/.python_history | grep "enumerate") && (cat ~/.python_history | grep "open") && (cat ~/.python_history | grep "with") && echo "True"
