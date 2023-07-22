#!/bin/zsh
(cd /home/labex/project/git-playground && git log --oneline | less -R | grep "Merge branch 'feature1'") && (cat ~/.zsh_history | grep -v grep | grep "git log") && (cat ~/.zsh_history | grep -v grep | grep "no-merges") && echo "True"
