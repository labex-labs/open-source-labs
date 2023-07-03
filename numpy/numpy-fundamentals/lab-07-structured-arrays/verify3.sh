#!/bin/zsh

cd ~/project
git diff | grep -E '\[.*[0-9].*,'
