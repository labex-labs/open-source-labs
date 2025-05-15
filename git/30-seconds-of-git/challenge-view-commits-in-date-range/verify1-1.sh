#!/bin/bash
(cat ~/.zsh_history | grep -v grep | grep "12 weeks ago") && (cat ~/.zsh_history | grep -v grep | grep "Apr 27 2023") && (cat ~/.zsh_history | grep -v grep | grep "Apr 25 2023") && (cat ~/.zsh_history | grep -v grep | grep "git log") && echo "True"
