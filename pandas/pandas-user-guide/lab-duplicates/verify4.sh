#!/bin/zsh

cd ~/project
git diff | grep 'index'
git diff | grep 'columns'
git diff | grep 'is_unique'
git diff | grep 'duplicated'
