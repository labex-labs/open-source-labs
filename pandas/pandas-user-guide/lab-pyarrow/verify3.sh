#!/bin/zsh

cd ~/project
git diff | grep 'pyarrow'
git diff | grep 'list_'
git diff | grep 'Series'
git diff | grep 'ArrowDtype'
