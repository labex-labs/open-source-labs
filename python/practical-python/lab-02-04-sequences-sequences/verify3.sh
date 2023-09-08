#!/bin/zsh
((cat ~/.python_history | grep "] = [") || (cat ~/.python_history | grep "]=[")) && echo "True"
