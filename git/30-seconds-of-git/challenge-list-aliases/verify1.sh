#!/bin/zsh
history | grep "sed 's/^alias\.//g'" | tail -n 1 | sh | grep -q "st=status\|co=checkout\|rb=rebase" && echo "True"
