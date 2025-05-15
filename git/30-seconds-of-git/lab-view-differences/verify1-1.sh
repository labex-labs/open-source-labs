#!/bin/bash
(cat ~/.zsh_history | grep -v grep | grep "staged") && (cat ~/.zsh_history | grep -v grep | grep "git diff") && echo "True"
