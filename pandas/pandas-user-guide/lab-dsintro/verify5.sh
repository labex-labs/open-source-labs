#!/bin/zsh

cd ~/project
git diff | grep -E "\w+\s*=\s*\w+\s*\+\s*\w+"