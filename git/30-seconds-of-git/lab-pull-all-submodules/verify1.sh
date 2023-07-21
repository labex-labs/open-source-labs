#!/bin/zsh
(cat ~/.zsh_history | grep -v grep | grep "cd git-playground") && (cat ~/.zsh_history | grep -v grep | grep "git submodule update") && (cat ~/.zsh_history | grep -v grep | grep "remote") && echo "True"
