#!/bin/zsh
cd /home/labex/project
git clone https://github.com/labex-labs/git-playground.git
cd /home/labex/project/git-playground
git checkout -b one-branch
git checkout -b two-branch
git checkout -b three-branch
git checkout -b four-branch
git checkout -b five-branch
git checkout master

# Initialize .zsh_history
touch /home/labex/.zsh_history
