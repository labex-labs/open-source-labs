#!/bin/zsh

cd ~/project
git diff | grep 'numpy'
git diff | grep 'collections'
git diff | grep 'matplotlib'
