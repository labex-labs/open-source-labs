#!/bin/zsh

cd ~/project
git diff | grep 'pandas'
git diff | grep 'numpy'
git diff | grep 'Int64Dtype'
git diff | grep 'array'
git diff | grep -w 'Int64'
