#!/bin/zsh

cd ~/project
git diff | grep 'Series'
git diff | grep 'float32'
git diff | grep 'mean'
git diff | grep 'fillna'
