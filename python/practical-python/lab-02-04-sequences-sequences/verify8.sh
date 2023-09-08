#!/bin/zsh
(cat ~/.python_history | grep "for") && (cat ~/.python_history | grep "in") && (cat ~/.python_history | grep "range") && echo "True"
