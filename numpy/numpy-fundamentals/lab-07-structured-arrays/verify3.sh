#!/bin/zsh

cd ~/project
git diff | grep -E '\[.*[0-9].*,.*[0-9].*\]'
