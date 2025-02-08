#!/bin/zsh
(cat ~/.zsh_history | grep -v grep | grep "remote.origin.url") && (cat ~/.zsh_history | grep -v grep | grep "git config") && echo "True"
