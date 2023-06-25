#!/bin/zsh

cd ~/project
git diff | grep 'dtype'
git diff | grep 'int'
git diff | grep 'issubdtype'
git diff | grep 'integer'
git diff | grep 'floating'
