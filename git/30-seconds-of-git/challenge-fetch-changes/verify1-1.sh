#!/bin/bash
(cat ~/.zsh_history | grep -v grep | grep "git fetch") && (cat ~/.zsh_history | grep -v grep | grep "cd git-playground") && echo "True"
