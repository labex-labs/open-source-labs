#!/bin/zsh

cd ~/project
git diff | grep 'def'
git diff | grep 'get_window_extent'
git diff | grep 'set_position'
