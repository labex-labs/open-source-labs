#!/bin/zsh

cd ~/project
git diff | grep -w 'set_option'
git diff | grep 'precision'
