#!/bin/zsh
(cat ~/.zsh_history | grep -v grep | grep "1") && (cat ~/.zsh_history | grep -v grep | grep "git log") && echo "True"
