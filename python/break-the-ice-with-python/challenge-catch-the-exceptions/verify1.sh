#!/bin/zsh

cd /tmp && python3.6 catch_the_exceptions_test.py
cat /home/project/catch_the_exceptions.py | -E "try"
cat /home/project/catch_the_exceptions.py | -E "except"
