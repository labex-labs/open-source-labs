#!/bin/zsh

cd ~/project
git diff | grep 'subplots'
git diff | grep 'area'
git diff | grep 'savefig'
git diff | grep 'set_ylabel'
