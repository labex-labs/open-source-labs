#!/bin/zsh

cat ~/.python_history | grep -E "import.*simplemod"
cat ~/.python_history | grep -E "=.*simplemod"
cat ~/.python_history | grep "reload"
cat ~/.python_history | grep -E "isinstance"
