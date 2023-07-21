#!/bin/zsh

cd ~/project
git diff | grep 'get_xticklabels'
git diff | grep 'set'
git diff | grep 'setp'
