#!/bin/zsh

history_file="$HOME/.python_history"

if [[ -f "$history_file" ]]; then
    > "$history_file"
fi

cat ~/.python_history | grep "collections"
cat ~/.python_history | grep "namedtuple"
cat ~/.python_history | grep "inspect"
cat ~/.python_history | grep "getsource"
