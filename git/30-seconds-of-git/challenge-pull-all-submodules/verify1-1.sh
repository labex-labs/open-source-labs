#!/bin/bash
(cat ~/.zsh_history | grep -v grep | grep "git submodule update") && (cat ~/.zsh_history | grep -v grep | grep "remote") && echo "True"
