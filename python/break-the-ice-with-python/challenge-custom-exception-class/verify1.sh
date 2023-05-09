#!/bin/zsh

cd /tmp && python3 custom_exception_class_test.py
cat /home/labex/project/catch_the_exceptions.py | grep -E "try:"
cat /home/labex/project/catch_the_exceptions.py | grep -E "except:"
