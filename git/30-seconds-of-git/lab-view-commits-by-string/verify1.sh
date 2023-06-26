#!/bin/zsh
(cat ~/.zsh_history | grep -v grep | grep '-S"Git Playground"') && (cat ~/.zsh_history | grep -v grep | grep "git log") && echo "True"

