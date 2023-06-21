#!/bin/zsh

cd ~/project
git diff | grep 'pandas'
git diff | grep 'matplotlib'
git diff | grep 'read_csv'
git diff | grep 'rename'
git diff | grep 'columns'
