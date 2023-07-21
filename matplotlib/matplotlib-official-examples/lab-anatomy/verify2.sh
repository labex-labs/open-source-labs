#!/bin/zsh

cd ~/project
git diff | grep 'figure'
git diff | grep 'add_axes'
git diff | grep 'grid'
git diff | grep 'set_ylim'
