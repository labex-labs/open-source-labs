#!/bin/zsh
(cat ~/.zsh_history | grep "git config") && (cat ~/.zsh_history | grep ^alias\./) && echo "True"
