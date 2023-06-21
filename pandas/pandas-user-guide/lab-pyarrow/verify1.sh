#!/bin/zsh

cd ~/project
git diff | grep 'install'
git diff | grep 'pyarrow'
