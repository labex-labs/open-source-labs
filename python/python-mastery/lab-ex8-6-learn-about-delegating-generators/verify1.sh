#!/bin/zsh

cat /home/labex/project/cofollow.py | grep "assert"
cat /home/labex/project/cofollow.py | grep "isinstance"
cat ~/.python_history | grep "cofollow"
cat ~/.python_history | grep -E "@.*consumer"
cat ~/.python_history | grep "yield"
