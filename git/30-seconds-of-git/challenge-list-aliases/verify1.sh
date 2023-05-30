#!/bin/zsh
cat ~/.zsh_history | grep 'git config -l' | sed 's/^\s*[0-9]\+\s*//' | head -n 1 | xargs -I {} sh -c '{}' | grep -q "co=checkout" && grep -q "st=status" && grep -q "rb=rebase" && echo "True"
