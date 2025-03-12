#!/bin/bash
if grep -q "cd ~/project" ~/.zsh_history || grep -q "ls -la structly" ~/.zsh_history; then
  exit 0
else
  exit 1
fi
