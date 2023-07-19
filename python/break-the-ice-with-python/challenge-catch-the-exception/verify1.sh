#!/bin/zsh

cd /tmp && python3 catch_the_exception_test.py
cat /home/labex/project/catch_the_exception.py | grep -E "try:"
cat /home/labex/project/catch_the_exception.py | grep -E "except:"
