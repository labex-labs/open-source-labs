#!/bin/zsh

cd ~/project
git diff | grep 'io'
git diff | grep 'StringIO'
git diff | grep 'read_csv'
