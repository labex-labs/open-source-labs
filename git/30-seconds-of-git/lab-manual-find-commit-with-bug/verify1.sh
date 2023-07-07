#!/bin/zsh
(cat ~/.zsh_history | grep -v grep | grep "git bisect good") && (cat ~/.zsh_history | grep -v grep | grep "git bisect bad") && (cd /home/labex/project/git-playground && git bisect && git reflog | less -R | grep "checkout: moving from master to") && echo "True"
