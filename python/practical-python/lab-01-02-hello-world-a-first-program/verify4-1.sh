#!/bin/zsh
(cat ~/.zsh_history | grep -v grep | grep "python hello.py") && echo "True"
