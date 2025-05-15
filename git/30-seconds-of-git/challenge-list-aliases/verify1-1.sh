#!/bin/bash
(cat ~/.zsh_history | grep "sed") && (cat ~/.zsh_history | grep "git config") && (cat ~/.zsh_history | less -R | grep "alias") && echo "True"
