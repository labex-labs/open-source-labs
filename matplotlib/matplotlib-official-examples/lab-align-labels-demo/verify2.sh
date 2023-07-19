#!/bin/zsh

cd ~/project
git diff | grep 'figure'
git diff | grep 'set_xlabel'
git diff | grep 'tick_params'
