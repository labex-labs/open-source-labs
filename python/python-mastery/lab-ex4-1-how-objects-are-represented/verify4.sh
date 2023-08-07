#!/bin/zsh

cat ~/.python_history | grep  "__class__"
cat ~/.python_history | grep -E  "__dict__.*\[.*\].*\("
