#!/bin/zsh

cd ~/project
git diff | grep 'DataFrame'
git diff | grep 'iloc'
git diff | grep 'copy_on_write'
