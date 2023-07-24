#!/bin/zsh

cd ~/project
git diff | grep 'matplotlib'
git diff | grep 'numpy'
git diff | grep 'set_box_aspect'
