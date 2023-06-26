#!/bin/zsh

cd ~/project
git diff | grep 'to_parquet'
git diff | grep 'read_parquet'
git diff | grep 'copy'
git diff | grep 'astype'
git diff | grep 'to_numeric'
git diff | grep 'apply'
