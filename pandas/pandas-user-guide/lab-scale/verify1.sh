#!/bin/zsh

cd ~/project
git diff | grep 'pandas'
git diff | grep 'numpy'
git diff | grep 'date_range'
git diff | grep 'RandomState'
git diff | grep 'poisson'
git diff | grep 'DataFrame'
git diff | grep 'iloc'
git diff | grep 'concat'
git diff | grep 'rename'
git diff | grep 'to_parquet'
