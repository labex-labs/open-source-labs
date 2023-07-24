#!/bin/zsh

cd ~/project
git diff | grep 'float32'
git diff | grep 'int_'
git diff | grep 'arange'
git diff | grep 'uint8'
git diff | grep 'astype'
git diff | grep 'int8'
