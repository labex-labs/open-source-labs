#!/bin/zsh

cat ~/.python_history | grep  "from"
cat ~/.python_history | grep  "simplemod"
cat ~/.python_history | grep -E  "simplemod.*\..*\(.*\)"
