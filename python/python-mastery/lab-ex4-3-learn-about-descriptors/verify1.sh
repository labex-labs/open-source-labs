#!/bin/zsh

cat ~/.python_history | grep -E "=.*\("
cat ~/.python_history | grep "__dict__"
cat ~/.python_history | grep "__get__"
cat ~/.python_history | grep "__set__"
