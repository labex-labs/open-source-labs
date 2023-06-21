#!/bin/zsh

cd ~/project
git diff | grep 'dask'
git diff | grep 'read_parquet'
git diff | grep 'value_counts'
