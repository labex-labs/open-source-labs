#!/bin/zsh
(cat ~/.zsh_history | grep -v grep | grep "git add index.html style.css")&&(cat ~/.zsh_history | grep -v grep | grep "git add *.js")&&(cat ~/.zsh_history | grep -v grep | grep "git add .")&& echo "True"

