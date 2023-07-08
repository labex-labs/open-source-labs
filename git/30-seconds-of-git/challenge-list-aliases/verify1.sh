#!/bin/zsh
(cat ~/.zsh_history | grep "git config") && (cat ~/.zsh_history | less -R | grep "alias\.") && echo "True"
