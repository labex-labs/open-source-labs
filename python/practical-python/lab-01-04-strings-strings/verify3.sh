#!/bin/zsh
(grep -q "\N" ~/.python_history || grep -q "\x" ~/.python_history || grep -q "\u" ~/.python_history || grep -q "\U" ~/.python_history )&& echo "True"
