#!/bin/zsh
history | grep "git config -l | grep alias | sed 's/^alias\.//g'" | tail -n 1 | xargs -I {} sh -c "{} | grep -E '^(co=checkout|rb=rebase|st=status)$'"
