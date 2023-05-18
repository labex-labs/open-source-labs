#!/bin/zsh
cd /home/labex/project/git-playground
cat ~/.zsh_history | grep -E 'git\s+branch\s+--contains\s+d22f46b\s+' | tail -1 | xargs -I{} sh -c '{} | grep patch-1'
