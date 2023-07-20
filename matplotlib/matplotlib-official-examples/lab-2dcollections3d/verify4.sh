#!/bin/zsh

cd ~/project
git diff | grep 'set_zlabel'
git diff | grep 'view_init'
git diff | grep 'show'
