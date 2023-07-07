#!/bin/zsh

cd ~/project
git diff | grep 'numpy'
git diff | grep 'array'
git diff | grep 'view'
