#!/bin/zsh
cd /home/labex/project/git-playground && history | grep "git config -l" | tail -n 1 | tee output.txt | awk '{$1=""; print $0}' | sh | grep -q "co=checkout" && grep -q "st=status" && grep -q "rb=rebase" && echo "True"
