#!/bin/zsh

cd ~/project
git diff | grep -oE 'result\s*=\s*df.\s*\+\s*df.'
