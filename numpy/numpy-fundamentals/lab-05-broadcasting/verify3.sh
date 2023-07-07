#!/bin/zsh

cd ~/project
git diff | grep -E '=[[:space:]]*[0-9]\.'
