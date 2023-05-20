#!/bin/zsh
cd /home/labex/project/git-playground
if git config --list | grep -q "user.email=jane.doe@example.com" && git config --list | grep -q "user.name=Jane Doe"; then echo "True"; fi
