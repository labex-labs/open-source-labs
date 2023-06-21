#!/bin/zsh

cd ~/project
git diff | grep 'Series'
git diff | grep 'lower'
git diff | grep 'upper'
git diff | grep 'len'
