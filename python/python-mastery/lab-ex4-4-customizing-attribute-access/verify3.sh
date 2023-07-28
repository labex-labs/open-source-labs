#!/bin/zsh

history_file="$HOME/.python_history"

if [[ -f "$history_file" ]]; then
    > "$history_file"
fi
cat ~/.python_history | grep "__init__"
cat ~/.python_history | grep "__getattr__"
cat ~/.python_history | grep "getattr"
