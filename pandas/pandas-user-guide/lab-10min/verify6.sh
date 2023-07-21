#!/bin/zsh

cd ~/project
git diff | grep 'sort_index'
git diff | grep 'apply'
git diff | grep 'cumsum'
