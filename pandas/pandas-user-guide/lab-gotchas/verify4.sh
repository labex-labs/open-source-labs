#!/bin/zsh

cd ~/project
git diff | grep 'Series'
git diff | grep 'Int64Dtype'
git diff | grep 'reindex'
