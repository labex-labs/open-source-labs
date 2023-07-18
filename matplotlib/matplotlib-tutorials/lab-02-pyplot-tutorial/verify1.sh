#!/bin/zsh

cd ~/project
git diff | grep 'matplotlib'
git diff | grep 'plot'
git diff | grep 'ylabel'
git diff | grep 'show'
