#!/bin/zsh

cd ~/project
git diff | grep 'subplots'
git diff | grep 'plot'
git diff | grep 'set_ylim'
