#!/bin/zsh

cd ~/project
git diff | grep -E '[[:space:]]*>[[:space:]]*'
