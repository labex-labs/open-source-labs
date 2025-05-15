#!/bin/bash
(cat ~/.zsh_history | grep -v grep | grep "git diff") && (cat ~/.zsh_history | grep -v grep | grep "feature-1..feature-2") && echo "True"
