#!/bin/zsh
(cat ~/.zsh_history | grep -v grep | grep "git push -u") && (cat ~/.zsh_history | grep -v grep | grep "git config push.default current") && (cd /home/labex/project/git-playground && git log -r | grep "Add hello.txt") && echo "True"
