#!/bin/zsh

cd ~/project
git diff | grep 'numpy'
git diff | grep 'matplotlib'
git diff | grep 'get_sample_data'