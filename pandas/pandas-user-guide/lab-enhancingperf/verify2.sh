#!/bin/zsh

cd ~/project
git diff | grep 'def'
git diff | grep 'return'
git diff | grep '/'
git diff | grep '*'
git diff | grep 'for'
