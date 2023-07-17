#!/bin/zsh

cd ~/project
git diff | grep 'get_extent'
git diff | grep 'imshow'
git diff | grep 'set_ylim'
