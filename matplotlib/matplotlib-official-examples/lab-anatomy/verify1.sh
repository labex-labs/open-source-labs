#!/bin/zsh

cd ~/project
git diff | grep 'matplotlib'
git diff | grep 'numpy'
git diff | grep 'random'
git diff | grep 'linspace'
