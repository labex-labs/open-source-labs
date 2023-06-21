#!/bin/zsh

cd ~/project
git diff | grep 'DataFrame'
git diff | grep 'set_flags'
git diff | grep 'flags'
