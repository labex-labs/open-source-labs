#!/bin/zsh

cd ~/project
git diff | grep 'set_option'
git diff | grep 'max_rows'
git diff | grep 'precision'
git diff | grep 'pandas'
