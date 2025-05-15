#!/bin/bash
(cat ~/.zsh_history | grep -v grep | grep "git branch") && (cat ~/.zsh_history | grep -v grep | grep "sort=-committerdate") && echo "True"
