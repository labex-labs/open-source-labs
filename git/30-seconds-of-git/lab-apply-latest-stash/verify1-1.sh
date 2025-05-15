#!/bin/bash
(cat ~/.zsh_history | grep -v grep | grep "git stash") && (cat ~/.zsh_history | grep -v grep | grep "apply") && echo "True"
