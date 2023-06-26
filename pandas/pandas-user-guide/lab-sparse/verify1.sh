#!/bin/zsh

cd ~/project
git diff | grep 'pandas'
git diff | grep 'numpy'
git diff | grep 'randn'
git diff | grep 'Series'
git diff | grep 'SparseArray'
