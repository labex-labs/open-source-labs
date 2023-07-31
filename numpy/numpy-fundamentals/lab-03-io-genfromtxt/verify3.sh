#!/bin/zsh

cd ~/project
git diff | grep -E 'genfromtxt.*\('
