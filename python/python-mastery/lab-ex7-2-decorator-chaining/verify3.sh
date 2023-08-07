#!/bin/zsh

cat /home/labex/project/spam.py | grep "logcall"
cat /home/labex/project/spam.py | grep -E "@.*logged"
cat /home/labex/project/spam.py | grep -E "@.*classmethod"
cat /home/labex/project/spam.py | grep -E "@.*staticmethod"
cat /home/labex/project/spam.py | grep -E "@.*property"
cat /home/labex/project/spam.py | grep "def"
