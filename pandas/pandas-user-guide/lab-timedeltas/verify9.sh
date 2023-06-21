#!/bin/zsh

cd ~/project
git diff | grep 'TimedeltaIndex'
git diff | grep 'date_range'
git diff | grep 'to_list'
