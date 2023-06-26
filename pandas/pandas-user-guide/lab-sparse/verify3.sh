#!/bin/zsh

cd ~/project
git diff | grep 'SparseDtype'
git diff | grep 'dtype'
git diff | grep 'Timestamp'
git diff | grep 'datetime64'
