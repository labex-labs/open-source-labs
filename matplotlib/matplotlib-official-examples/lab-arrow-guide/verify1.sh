#!/bin/zsh

cd ~/project
git diff | grep 'matplotlib'
git diff | grep 'FancyArrowPatch'
git diff | grep 'add_patch'
