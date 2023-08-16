#!/bin/zsh

cd ~/project
git diff | grep 'numpy'
git diff | grep 'functools'
git diff | grep 'cycler'
git diff | grep 'matplotlib'
