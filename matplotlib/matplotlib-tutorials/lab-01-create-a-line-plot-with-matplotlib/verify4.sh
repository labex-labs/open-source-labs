#!/bin/zsh

cd ~/project
git diff | grep 'xlabel'
git diff | grep 'title'
git diff | grep 'legend'
