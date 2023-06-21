#!/bin/zsh

cd ~/project
git diff | grep 'Series'
git diff | grep 'set_flags'
git diff | grep 'DataFrame'
