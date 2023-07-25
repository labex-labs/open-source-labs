#!/bin/zsh

cd ~/project
git diff | grep 'left_on'
git diff | grep 'parameter'
git diff | grep 'right_on'
git diff | grep 'id'
