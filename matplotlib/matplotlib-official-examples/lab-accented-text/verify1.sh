#!/bin/zsh

cd ~/project
git diff | grep 'matplotlib'
git diff | grep 'subplots'
git diff | grep 'tight_layout'
