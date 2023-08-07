#!/bin/zsh

cat ~/.python_history | grep -E "\..*="
cat ~/.python_history | grep "importlib"
cat ~/.python_history | grep "reload"
cat ~/.python_history | grep "sys"
cat ~/.python_history | grep "modules"
cat ~/.python_history | grep "del"
