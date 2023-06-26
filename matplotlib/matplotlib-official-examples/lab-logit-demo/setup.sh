#!/bin/zsh
cd ~/project
git init
git config --global user.email 'labex@labex.io'
git config --global user.name 'LabEx'
git add .
git commit -m 'init'

pip install matplotlib
