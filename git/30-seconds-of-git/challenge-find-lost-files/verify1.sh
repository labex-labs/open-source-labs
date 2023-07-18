#!/bin/zsh
(cat ~/.zsh_history | grep -v grep | grep "git fsck --lost-found") && (cat ~/.zsh_history | grep -v grep | grep "cd git-playground") && echo "True"
