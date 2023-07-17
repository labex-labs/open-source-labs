#!/bin/zsh

cd ~/project
git diff | grep 'set_xlabel'
git diff | grep 'set_title'
