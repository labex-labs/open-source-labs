#!/bin/zsh

cd ~/project
git diff | grep 'set_ylabel'
git diff | grep 'text'
git diff | grep 'show'
