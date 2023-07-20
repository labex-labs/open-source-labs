#!/bin/zsh

cd ~/project
git diff | grep 'matplotlib'
git diff | grep 'numpy'
git diff | grep 'add_subplot'
