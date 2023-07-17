#!/bin/zsh

cd ~/project
git diff | grep 'rcParams'
git diff | grep 'subplots_adjust'
git diff | grep 'toggle'
