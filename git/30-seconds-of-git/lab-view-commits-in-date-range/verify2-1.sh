#!/bin/bash

cat ~/.zsh_history | grep -v grep | grep "git log" && echo "True"
