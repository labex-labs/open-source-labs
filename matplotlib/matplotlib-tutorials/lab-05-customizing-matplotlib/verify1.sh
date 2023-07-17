#!/bin/zsh

cd ~/project
git diff | grep 'matplotlib'
git diff | grep 'rcParams'
git diff | grep 'show'
