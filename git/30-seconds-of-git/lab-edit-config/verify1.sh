#!/bin/zsh
((cat ~/.zsh_history | grep -v grep | grep "git config --global -e") || (cat ~/.zsh_history | grep -v grep | grep "git configuration --global -e")) && echo "True"
