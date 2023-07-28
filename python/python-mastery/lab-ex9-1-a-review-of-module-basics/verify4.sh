#!/bin/zsh

history_file="$HOME/.python_history"

if [[ -f "$history_file" ]]; then
    > "$history_file"
fi

cat ~/.python_history | grep  "from"
cat ~/.python_history | grep  "simplemod"
cat ~/.python_history | grep -E  "simplemod.*\..*\(.*\)"
