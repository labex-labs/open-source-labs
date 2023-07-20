#!/bin/zsh

cd ~/project
git diff | grep 'figure'
git diff | grep 'subplot'
git diff | grep 'suptitle'
