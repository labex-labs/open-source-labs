#!/bin/bash
(cat ~/.zsh_history | grep -v grep | grep "git shortlog") && (cat ~/.zsh_history | grep -v grep | grep ".HEAD") && echo "True"
