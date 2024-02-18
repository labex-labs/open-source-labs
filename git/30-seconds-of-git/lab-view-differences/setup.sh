#!/bin/zsh
cd /home/labex/project
git clone https://github.com/labex-labs/git-playground.git
cd /home/labex/project/git-playground
echo "hello,world" >> README.md
git add README.md
echo "hello,labex" >> file1.txt

# Initialize .zsh_history
touch /home/labex/.zsh_history
