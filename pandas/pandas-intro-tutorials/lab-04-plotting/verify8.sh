#!/bin/zsh

cd ~/project
git diff | grep 'savefig'
git diff | grep 'set_ylabel'
ls /home/labex/project/*.png