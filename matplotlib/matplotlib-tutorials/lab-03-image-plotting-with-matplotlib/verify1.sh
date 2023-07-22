#!/bin/zsh

cd ~/project
git diff | grep 'PIL'
git diff | grep 'matplotlib'
git diff | grep 'numpy'
git diff | grep 'asarray'
