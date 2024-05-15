#!/bin/zsh
(cat ~/.zsh_history | grep -v grep | grep ".HEAD") && (cat ~/.zsh_history | grep -v grep | grep "git shortlog") && echo "True"
