#!/bin/zsh

cd ~/project
git diff | grep 'copy_on_write'
git diff | grep 'DataFrame'
git diff | grep 'iloc'
