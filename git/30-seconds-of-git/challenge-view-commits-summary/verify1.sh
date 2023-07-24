#!/bin/zsh
(cat ~/.zsh_history | grep -v grep | grep "oneline") && (cat ~/.zsh_history | grep -v grep | grep "git log") && echo "True"

