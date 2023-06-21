#!/bin/zsh

cd ~/project
git diff | grep 'DataFrame'
git diff | grep 'to_dense'
git diff | grep 'SparseDtype'
git diff | grep 'astype'
