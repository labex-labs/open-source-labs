#!/bin/zsh

cd /tmp && python3 catch_the_exceptions_test.py
cat /home/labex/project/catch_the_exceptions.py | grep -E "try:"
cat /home/labex/project/catch_the_exceptions.py | grep -E "except:"
