#!/bin/zsh
cd /home/labex/project/git-playground
history | grep "git config -l" | awk '{$1=""; print $0}' | tail -n 1 | xargs -0 sh -c | grep -q "st=status" && grep -q "co=checkout" && grep -q "rb=rebase" && echo "True"
