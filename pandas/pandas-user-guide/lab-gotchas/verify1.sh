#!/bin/zsh

cd ~/project
git diff | grep 'numpy'
git diff | grep 'pandas'
git diff | grep 'DataFrame'
git diff | grep 'randint'
git diff | grep 'int64'
git diff | grep 'bool'
git diff | grep 'for'
git diff | grep 'astype'
