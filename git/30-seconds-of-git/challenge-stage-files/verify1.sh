#!/bin/zsh
(cat ~/.zsh_history | grep -v grep | grep "git add .") && (cat ~/.zsh_history | grep -v grep | grep "git add *.js") && (cat ~/.zsh_history | grep -v grep | grep "git add index.html style.css") && echo "True"
