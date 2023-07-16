#!/bin/zsh

cd ~/project
git diff | grep 'subplots'
git diff | grep 'linspace'
git diff | grep 'set_ylim'
