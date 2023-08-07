#!/bin/zsh

cat ~/.python_history | grep "class"
cat ~/.python_history | grep "def"
cat ~/.python_history | grep -E "=.*\("
