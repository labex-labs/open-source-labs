#!/bin/zsh

cd ~/project
git diff | grep 'Series'
git diff | grep '|'
git diff | grep 'get_dummies'
