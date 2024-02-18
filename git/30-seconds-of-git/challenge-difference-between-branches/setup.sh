#!/bin/zsh
cd /home/labex/project
git clone https://github.com/labex-labs/git-playground.git
cd /home/labex/project/git-playground
git branch feature-1
git branch feature-2

# Initialize .zsh_history
touch /home/labex/.zsh_history
