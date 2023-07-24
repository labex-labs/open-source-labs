#!/bin/zsh

cd ~/project
git diff | grep 'options'
git diff | grep 'display'
git diff | grep 'max_rows'
