#!/bin/zsh

cd /tmp && python3 catch_the_exceptions_test.py
cat /home/labex/project/catch_the_exceptions.py | -E "try"
cat /home/labex/project/catch_the_exceptions.py | -E "except"
