#!/bin/zsh
cat ~/.zsh_history | grep -v grep | grep "git pull"
cat ~/.zsh_history | grep -v grep | grep "git checkout"
