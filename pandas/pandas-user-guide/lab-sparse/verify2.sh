#!/bin/zsh

cd ~/project
git diff | grep 'DataFrame'
git diff | grep 'randn'
git diff | grep 'iloc'
git diff | grep 'astype'
git diff | grep 'SparseDtype'
