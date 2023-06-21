#!/bin/zsh

cd ~/project
git diff | grep 'to_csv'
git diff | grep 'read_csv'
