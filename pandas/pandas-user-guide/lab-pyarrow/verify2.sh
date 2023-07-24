#!/bin/zsh

cd ~/project
git diff | grep 'pandas'
git diff | grep 'Series'
git diff | grep 'Index'
git diff | grep 'DataFrame'
