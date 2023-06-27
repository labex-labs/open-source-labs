#!/bin/zsh

cd ~/project
git diff | grep 'pandas'
git diff | grep 'numpy'
git diff | grep 'DataFrame'
git diff | grep 'randn'
git diff | grep '>'
git diff | grep 'reindex'
