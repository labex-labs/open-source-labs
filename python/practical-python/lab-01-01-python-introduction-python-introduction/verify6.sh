#!/bin/zsh
((cat ~/.python_history | grep "12 + 20") || (cat ~/.python_history | grep "(3 + 4
         + 5 + 6)") || (cat ~/.python_history | grep "for i in range(5):)) && echo "True"