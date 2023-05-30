#!/bin/zsh
cd /home/labex/project/git-playground && history | grep "git config -l" | awk '{$1=""; print $1}' | tail -n 1 | xargs -I {} sh -c '!{}' | grep -q "co=checkout" && grep -q "st=status" && grep -q "rb=rebase" && echo "True"
