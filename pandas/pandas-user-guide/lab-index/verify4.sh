#!/bin/zsh

cd ~/project
git diff | grep 'DataFrame'
git diff | grep 'nan'
git diff | grep 'fillna'
