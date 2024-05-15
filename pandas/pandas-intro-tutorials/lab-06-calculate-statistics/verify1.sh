#!/bin/zsh

cd ~/project
git diff | grep 'pandas'
git diff | grep 'read_csv'
git diff | grep 'head'
