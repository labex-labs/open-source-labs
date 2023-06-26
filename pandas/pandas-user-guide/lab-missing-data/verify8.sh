#!/bin/zsh

cd ~/project
git diff | grep 'Series'
git diff | grep 'dtype'
git diff | grep 'Int64'
